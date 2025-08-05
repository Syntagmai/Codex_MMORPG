#!/usr/bin/env python3
"""
Script de Testes Automatizados - Validação do Conhecimento Integrado
Task 16.11: Validação e Testes do Conhecimento Integrado
"""

import os
import json
import time
from datetime import datetime

class KnowledgeValidationSuite:
    """Suite de testes para validação do conhecimento integrado"""
    
    def __init__(self):
        self.results = {
            "total_tests": 0,
            "passed_tests": 0,
            "failed_tests": 0,
            "test_details": [],
            "start_time": datetime.now(),
            "end_time": None
        }
        
    def run_test(self, test_name, test_function):
        """Executa um teste individual"""
        self.results["total_tests"] += 1
        
        try:
            result = test_function()
            if result.get("success", False):
                self.results["passed_tests"] += 1
                status = "✅ PASSED"
            else:
                self.results["failed_tests"] += 1
                status = "❌ FAILED"
                
            test_detail = {
                "name": test_name,
                "status": status,
                "result": result,
                "timestamp": datetime.now().isoformat()
            }
            self.results["test_details"].append(test_detail)
            
            print(f"{status} {test_name}")
            return result
            
        except Exception as e:
            self.results["failed_tests"] += 1
            test_detail = {
                "name": test_name,
                "status": "❌ ERROR",
                "error": str(e),
                "timestamp": datetime.now().isoformat()
            }
            self.results["test_details"].append(test_detail)
            
            print(f"❌ ERROR {test_name}: {e}")
            return {"success": False, "error": str(e)}
    
    def test_game_store_knowledge(self):
        """Testa conhecimento do Game Store"""
        print("\n🧪 Testando conhecimento do Game Store...")
        
        # Verificar se os arquivos de documentação existem
        files_to_check = [
            "wiki/docs/game_store_system_analysis.md",
            "wiki/docs/practical_guides/game_store_practical_guide.md"
        ]
        
        missing_files = []
        for file_path in files_to_check:
            if not os.path.exists(file_path):
                missing_files.append(file_path)
        
        if missing_files:
            return {
                "success": False,
                "error": f"Arquivos faltando: {missing_files}",
                "missing_files": missing_files
            }
        
        # Verificar conteúdo dos arquivos
        try:
            with open("wiki/docs/practical_guides/game_store_practical_guide.md", 'r', encoding='utf-8') as f:
                content = f.read()
                
            # Verificar se contém exemplos de código
            if "```lua" not in content:
                return {
                    "success": False,
                    "error": "Guias práticos não contêm exemplos de código Lua"
                }
            
            # Verificar se contém casos de uso
            if "Caso de Uso" not in content:
                return {
                    "success": False,
                    "error": "Guias práticos não contêm casos de uso"
                }
                
            return {
                "success": True,
                "files_checked": len(files_to_check),
                "content_validation": "passed",
                "examples_found": content.count("```lua"),
                "use_cases_found": content.count("Caso de Uso")
            }
            
        except Exception as e:
            return {
                "success": False,
                "error": f"Erro ao ler arquivos: {e}"
            }
    
    def test_extended_opcode_knowledge(self):
        """Testa conhecimento do Extended Opcode"""
        print("\n🔌 Testando conhecimento do Extended Opcode...")
        
        files_to_check = [
            "wiki/docs/extended_opcode_system_analysis.md",
            "wiki/docs/practical_guides/extended_opcode_practical_guide.md"
        ]
        
        missing_files = []
        for file_path in files_to_check:
            if not os.path.exists(file_path):
                missing_files.append(file_path)
        
        if missing_files:
            return {
                "success": False,
                "error": f"Arquivos faltando: {missing_files}",
                "missing_files": missing_files
            }
        
        try:
            with open("wiki/docs/practical_guides/extended_opcode_practical_guide.md", 'r', encoding='utf-8') as f:
                content = f.read()
                
            # Verificar se contém exemplos de fragmentação
            if "fragmentData" not in content:
                return {
                    "success": False,
                    "error": "Guias não contêm exemplos de fragmentação"
                }
            
            # Verificar se contém exemplos de callbacks
            if "registerCallback" not in content:
                return {
                    "success": False,
                    "error": "Guias não contêm exemplos de callbacks"
                }
                
            return {
                "success": True,
                "files_checked": len(files_to_check),
                "fragmentation_examples": content.count("fragmentData"),
                "callback_examples": content.count("registerCallback"),
                "json_examples": content.count("processJsonData")
            }
            
        except Exception as e:
            return {
                "success": False,
                "error": f"Erro ao ler arquivos: {e}"
            }
    
    def test_communication_knowledge(self):
        """Testa conhecimento de comunicação cliente-servidor"""
        print("\n🌐 Testando conhecimento de comunicação...")
        
        files_to_check = [
            "wiki/docs/client_server_communication_analysis.md",
            "wiki/docs/practical_guides/communication_practical_guide.md"
        ]
        
        missing_files = []
        for file_path in files_to_check:
            if not os.path.exists(file_path):
                missing_files.append(file_path)
        
        if missing_files:
            return {
                "success": False,
                "error": f"Arquivos faltando: {missing_files}",
                "missing_files": missing_files
            }
        
        try:
            with open("wiki/docs/practical_guides/communication_practical_guide.md", 'r', encoding='utf-8') as f:
                content = f.read()
                
            # Verificar se contém exemplos de autenticação
            if "authentication" not in content.lower():
                return {
                    "success": False,
                    "error": "Guias não contêm exemplos de autenticação"
                }
            
            # Verificar se contém exemplos de sincronização
            if "sync" not in content.lower():
                return {
                    "success": False,
                    "error": "Guias não contêm exemplos de sincronização"
                }
                
            return {
                "success": True,
                "files_checked": len(files_to_check),
                "authentication_examples": content.lower().count("authentication"),
                "sync_examples": content.lower().count("sync"),
                "error_handling": content.lower().count("error")
            }
            
        except Exception as e:
            return {
                "success": False,
                "error": f"Erro ao ler arquivos: {e}"
            }
    
    def test_coins_economy_knowledge(self):
        """Testa conhecimento de coins e economia"""
        print("\n💰 Testando conhecimento de coins e economia...")
        
        files_to_check = [
            "wiki/docs/coins_economy_system_analysis.md",
            "wiki/docs/practical_guides/coins_economy_practical_guide.md"
        ]
        
        missing_files = []
        for file_path in files_to_check:
            if not os.path.exists(file_path):
                missing_files.append(file_path)
        
        if missing_files:
            return {
                "success": False,
                "error": f"Arquivos faltando: {missing_files}",
                "missing_files": missing_files
            }
        
        try:
            with open("wiki/docs/practical_guides/coins_economy_practical_guide.md", 'r', encoding='utf-8') as f:
                content = f.read()
                
            # Verificar se contém exemplos de transferência
            if "transfer" not in content.lower():
                return {
                    "success": False,
                    "error": "Guias não contêm exemplos de transferência"
                }
            
            # Verificar se contém exemplos de transações
            if "transaction" not in content.lower():
                return {
                    "success": False,
                    "error": "Guias não contêm exemplos de transações"
                }
                
            return {
                "success": True,
                "files_checked": len(files_to_check),
                "transfer_examples": content.lower().count("transfer"),
                "transaction_examples": content.lower().count("transaction"),
                "validation_examples": content.lower().count("validation")
            }
            
        except Exception as e:
            return {
                "success": False,
                "error": f"Erro ao ler arquivos: {e}"
            }
    
    def test_ui_interface_knowledge(self):
        """Testa conhecimento de UI e interface"""
        print("\n🎨 Testando conhecimento de UI e interface...")
        
        files_to_check = [
            "wiki/docs/ui_interface_system_analysis.md",
            "wiki/docs/practical_guides/ui_interface_practical_guide.md"
        ]
        
        missing_files = []
        for file_path in files_to_check:
            if not os.path.exists(file_path):
                missing_files.append(file_path)
        
        if missing_files:
            return {
                "success": False,
                "error": f"Arquivos faltando: {missing_files}",
                "missing_files": missing_files
            }
        
        try:
            with open("wiki/docs/practical_guides/ui_interface_practical_guide.md", 'r', encoding='utf-8') as f:
                content = f.read()
                
            # Verificar se contém exemplos de modais
            if "modal" not in content.lower():
                return {
                    "success": False,
                    "error": "Guias não contêm exemplos de modais"
                }
            
            # Verificar se contém exemplos de controllers
            if "controller" not in content.lower():
                return {
                    "success": False,
                    "error": "Guias não contêm exemplos de controllers"
                }
                
            return {
                "success": True,
                "files_checked": len(files_to_check),
                "modal_examples": content.lower().count("modal"),
                "controller_examples": content.lower().count("controller"),
                "interface_examples": content.lower().count("interface")
            }
            
        except Exception as e:
            return {
                "success": False,
                "error": f"Erro ao ler arquivos: {e}"
            }
    
    def test_events_callbacks_knowledge(self):
        """Testa conhecimento de eventos e callbacks"""
        print("\n📡 Testando conhecimento de eventos e callbacks...")
        
        files_to_check = [
            "wiki/docs/events_callbacks_system_analysis.md",
            "wiki/docs/practical_guides/events_callbacks_practical_guide.md"
        ]
        
        missing_files = []
        for file_path in files_to_check:
            if not os.path.exists(file_path):
                missing_files.append(file_path)
        
        if missing_files:
            return {
                "success": False,
                "error": f"Arquivos faltando: {missing_files}",
                "missing_files": missing_files
            }
        
        try:
            with open("wiki/docs/practical_guides/events_callbacks_practical_guide.md", 'r', encoding='utf-8') as f:
                content = f.read()
                
            # Verificar se contém exemplos de eventos
            if "event" not in content.lower():
                return {
                    "success": False,
                    "error": "Guias não contêm exemplos de eventos"
                }
            
            # Verificar se contém exemplos de callbacks
            if "callback" not in content.lower():
                return {
                    "success": False,
                    "error": "Guias não contêm exemplos de callbacks"
                }
                
            return {
                "success": True,
                "files_checked": len(files_to_check),
                "event_examples": content.lower().count("event"),
                "callback_examples": content.lower().count("callback"),
                "g_game_examples": content.lower().count("g_game")
            }
            
        except Exception as e:
            return {
                "success": False,
                "error": f"Erro ao ler arquivos: {e}"
            }
    
    def test_modules_loading_knowledge(self):
        """Testa conhecimento de módulos e carregamento"""
        print("\n📦 Testando conhecimento de módulos e carregamento...")
        
        files_to_check = [
            "wiki/docs/modules_loading_system_analysis.md",
            "wiki/docs/practical_guides/modules_loading_practical_guide.md"
        ]
        
        missing_files = []
        for file_path in files_to_check:
            if not os.path.exists(file_path):
                missing_files.append(file_path)
        
        if missing_files:
            return {
                "success": False,
                "error": f"Arquivos faltando: {missing_files}",
                "missing_files": missing_files
            }
        
        try:
            with open("wiki/docs/practical_guides/modules_loading_practical_guide.md", 'r', encoding='utf-8') as f:
                content = f.read()
                
            # Verificar se contém exemplos de módulos
            if "module" not in content.lower():
                return {
                    "success": False,
                    "error": "Guias não contêm exemplos de módulos"
                }
            
            # Verificar se contém exemplos de dependências
            if "dependency" not in content.lower():
                return {
                    "success": False,
                    "error": "Guias não contêm exemplos de dependências"
                }
                
            return {
                "success": True,
                "files_checked": len(files_to_check),
                "module_examples": content.lower().count("module"),
                "dependency_examples": content.lower().count("dependency"),
                "loading_examples": content.lower().count("loading")
            }
            
        except Exception as e:
            return {
                "success": False,
                "error": f"Erro ao ler arquivos: {e}"
            }
    
    def test_validation_security_knowledge(self):
        """Testa conhecimento de validação e segurança"""
        print("\n🔒 Testando conhecimento de validação e segurança...")
        
        files_to_check = [
            "wiki/docs/validation_security_system_analysis.md",
            "wiki/docs/practical_guides/validation_security_practical_guide.md"
        ]
        
        missing_files = []
        for file_path in files_to_check:
            if not os.path.exists(file_path):
                missing_files.append(file_path)
        
        if missing_files:
            return {
                "success": False,
                "error": f"Arquivos faltando: {missing_files}",
                "missing_files": missing_files
            }
        
        try:
            with open("wiki/docs/practical_guides/validation_security_practical_guide.md", 'r', encoding='utf-8') as f:
                content = f.read()
                
            # Verificar se contém exemplos de validação
            if "validation" not in content.lower():
                return {
                    "success": False,
                    "error": "Guias não contêm exemplos de validação"
                }
            
            # Verificar se contém exemplos de segurança
            if "security" not in content.lower():
                return {
                    "success": False,
                    "error": "Guias não contêm exemplos de segurança"
                }
                
            return {
                "success": True,
                "files_checked": len(files_to_check),
                "validation_examples": content.lower().count("validation"),
                "security_examples": content.lower().count("security"),
                "authentication_examples": content.lower().count("authentication")
            }
            
        except Exception as e:
            return {
                "success": False,
                "error": f"Erro ao ler arquivos: {e}"
            }
    
    def test_knowledge_integration(self):
        """Testa integração do conhecimento"""
        print("\n🧠 Testando integração do conhecimento...")
        
        files_to_check = [
            "wiki/docs/knowledge_integration_code_creator_analysis.md",
            "wiki/docs/practical_guides/knowledge_integration_practical_guide.md"
        ]
        
        missing_files = []
        for file_path in files_to_check:
            if not os.path.exists(file_path):
                missing_files.append(file_path)
        
        if missing_files:
            return {
                "success": False,
                "error": f"Arquivos faltando: {missing_files}",
                "missing_files": missing_files
            }
        
        try:
            with open("wiki/docs/practical_guides/knowledge_integration_practical_guide.md", 'r', encoding='utf-8') as f:
                content = f.read()
                
            # Verificar se contém exemplos de templates
            if "template" not in content.lower():
                return {
                    "success": False,
                    "error": "Guias não contêm exemplos de templates"
                }
            
            # Verificar se contém exemplos de geração de código
            if "geração" not in content.lower() and "generate" not in content.lower():
                return {
                    "success": False,
                    "error": "Guias não contêm exemplos de geração de código"
                }
                
            return {
                "success": True,
                "files_checked": len(files_to_check),
                "template_examples": content.lower().count("template"),
                "generation_examples": content.lower().count("geração") + content.lower().count("generate"),
                "integration_examples": content.lower().count("integration")
            }
            
        except Exception as e:
            return {
                "success": False,
                "error": f"Erro ao ler arquivos: {e}"
            }
    
    def run_all_tests(self):
        """Executa todos os testes"""
        print("🚀 Iniciando suite de testes de validação do conhecimento...")
        print("=" * 60)
        
        tests = [
            ("Game Store Knowledge", self.test_game_store_knowledge),
            ("Extended Opcode Knowledge", self.test_extended_opcode_knowledge),
            ("Communication Knowledge", self.test_communication_knowledge),
            ("Coins Economy Knowledge", self.test_coins_economy_knowledge),
            ("UI Interface Knowledge", self.test_ui_interface_knowledge),
            ("Events Callbacks Knowledge", self.test_events_callbacks_knowledge),
            ("Modules Loading Knowledge", self.test_modules_loading_knowledge),
            ("Validation Security Knowledge", self.test_validation_security_knowledge),
            ("Knowledge Integration", self.test_knowledge_integration)
        ]
        
        for test_name, test_function in tests:
            self.run_test(test_name, test_function)
            time.sleep(0.5)  # Pequena pausa entre testes
        
        self.results["end_time"] = datetime.now()
        self.results["duration"] = (self.results["end_time"] - self.results["start_time"]).total_seconds()
        self.results["success_rate"] = (self.results["passed_tests"] / self.results["total_tests"]) * 100
        
        return self.results
    
    def generate_report(self):
        """Gera relatório final"""
        print("\n" + "=" * 60)
        print("📊 RELATÓRIO FINAL DE VALIDAÇÃO")
        print("=" * 60)
        
        print(f"📈 Total de Testes: {self.results['total_tests']}")
        print(f"✅ Testes Passaram: {self.results['passed_tests']}")
        print(f"❌ Testes Falharam: {self.results['failed_tests']}")
        print(f"📊 Taxa de Sucesso: {self.results['success_rate']:.1f}%")
        print(f"⏱️ Duração Total: {self.results['duration']:.2f} segundos")
        
        print("\n📋 Detalhes dos Testes:")
        for test in self.results["test_details"]:
            print(f"  {test['status']} {test['name']}")
            if "error" in test:
                print(f"    Erro: {test['error']}")
        
        # Salvar relatório
        report_file = "wiki/docs/validation_tests/test_results.json"
        os.makedirs(os.path.dirname(report_file), exist_ok=True)
        
        with open(report_file, 'w', encoding='utf-8') as f:
            json.dump(self.results, f, indent=2, default=str)
        
        print(f"\n💾 Relatório salvo em: {report_file}")
        
        return self.results

def main():
    """Função principal"""
    suite = KnowledgeValidationSuite()
    results = suite.run_all_tests()
    suite.generate_report()
    
    if results["success_rate"] >= 95:
        print("\n🎉 VALIDAÇÃO CONCLUÍDA COM SUCESSO!")
        print("✅ Conhecimento integrado validado com excelência")
        return 0
    else:
        print("\n⚠️ VALIDAÇÃO CONCLUÍDA COM PROBLEMAS!")
        print("❌ Alguns testes falharam - revisão necessária")
        return 1

if __name__ == "__main__":
    exit(main()) 