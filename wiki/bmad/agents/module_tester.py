#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
🧪 Module Tester Agent
Responsável por testar e validar módulos OTClient gerados
"""

import os
import json
import re
import ast
import subprocess
import tempfile
from pathlib import Path
from typing import Dict, List, Any, Optional, Tuple
from datetime import datetime
from difflib import unified_diff

class ModuleTesterAgent:
    """Agente especializado em teste e validação de módulos OTClient"""
    
    def __init__(self, workspace_path: str = None):
        self.workspace_path = workspace_path or os.getcwd()
        # Ajustar caminho para encontrar módulos na raiz do projeto
        if os.path.basename(self.workspace_path) == "bmad":
            # Se estamos na pasta bmad, subir um nível
            self.workspace_path = os.path.dirname(self.workspace_path)
        if os.path.basename(self.workspace_path) == "wiki":
            # Se estamos na pasta wiki, subir um nível
            self.workspace_path = os.path.dirname(self.workspace_path)
        
        self.modules_path = os.path.join(self.workspace_path, "modules")
        self.wiki_path = os.path.join(self.workspace_path, "wiki")
        self.results_path = os.path.join(self.workspace_path, "wiki/bmad/results")
        
        # Criar diretórios se não existirem
        os.makedirs(self.results_path, exist_ok=True)
        os.makedirs(os.path.join(self.results_path, "test_reports"), exist_ok=True)
        
        # Critérios de teste
        self.test_criteria = {
            "syntax_check": True,
            "structure_validation": True,
            "dependency_check": True,
            "compatibility_test": True,
            "performance_test": True,
            "security_test": True
        }
        
        # Padrões de erro conhecidos
        self.error_patterns = {
            "syntax_errors": [
                r"unexpected symbol",
                r"unexpected end",
                r"unexpected token",
                r"missing 'end'",
                r"unclosed string",
                r"invalid escape sequence"
            ],
            "runtime_errors": [
                r"attempt to call",
                r"attempt to index",
                r"attempt to perform arithmetic",
                r"bad argument",
                r"invalid key"
            ],
            "otclient_errors": [
                r"g_\w+ is nil",
                r"module not found",
                r"function not found",
                r"widget not found"
            ]
        }
    
    def test_module_variations(self, variations: List[Dict[str, Any]], 
                             original_analysis: Dict[str, Any]) -> Dict[str, Any]:
        """
        Testa todas as variações de um módulo
        
        Args:
            variations: Lista de variações geradas
            original_analysis: Análise do módulo original
            
        Returns:
            Relatório completo de testes
        """
        print(f"🧪 Testando {len(variations)} variações de módulo")
        
        test_report = {
            "test_date": datetime.now().isoformat(),
            "original_module": original_analysis["module_name"],
            "total_variations": len(variations),
            "test_criteria": self.test_criteria,
            "variation_results": [],
            "summary": {},
            "recommendations": []
        }
        
        for variation in variations:
            print(f"🔍 Testando variação: {variation['variation_name']}")
            
            variation_result = self.test_single_variation(variation, original_analysis)
            test_report["variation_results"].append(variation_result)
        
        # Gerar resumo
        test_report["summary"] = self.generate_test_summary(test_report["variation_results"])
        
        # Gerar recomendações
        test_report["recommendations"] = self.generate_recommendations(test_report)
        
        # Salvar relatório
        self.save_test_report(original_analysis["module_name"], test_report)
        
        return test_report
    
    def test_single_variation(self, variation: Dict[str, Any], 
                            original_analysis: Dict[str, Any]) -> Dict[str, Any]:
        """Testa uma variação específica"""
        variation_result = {
            "variation_name": variation["variation_name"],
            "variation_id": variation["variation_id"],
            "test_results": {},
            "errors": [],
            "warnings": [],
            "quality_score": 0.0,
            "compatibility_score": 0.0,
            "performance_score": 0.0
        }
        
        # Teste 1: Verificação de sintaxe
        syntax_result = self.test_syntax(variation)
        variation_result["test_results"]["syntax"] = syntax_result
        
        # Teste 2: Validação de estrutura
        structure_result = self.test_structure(variation, original_analysis)
        variation_result["test_results"]["structure"] = structure_result
        
        # Teste 3: Verificação de dependências
        dependency_result = self.test_dependencies(variation)
        variation_result["test_results"]["dependencies"] = dependency_result
        
        # Teste 4: Teste de compatibilidade
        compatibility_result = self.test_compatibility(variation, original_analysis)
        variation_result["test_results"]["compatibility"] = compatibility_result
        
        # Teste 5: Análise de performance
        performance_result = self.test_performance(variation)
        variation_result["test_results"]["performance"] = performance_result
        
        # Teste 6: Análise de segurança
        security_result = self.test_security(variation)
        variation_result["test_results"]["security"] = security_result
        
        # Coletar erros e avisos
        variation_result["errors"] = self.collect_errors(variation_result["test_results"])
        variation_result["warnings"] = self.collect_warnings(variation_result["test_results"])
        
        # Calcular scores
        variation_result["quality_score"] = self.calculate_quality_score(variation_result)
        variation_result["compatibility_score"] = self.calculate_compatibility_score(variation_result)
        variation_result["performance_score"] = self.calculate_performance_score(variation_result)
        
        return variation_result
    
    def test_syntax(self, variation: Dict[str, Any]) -> Dict[str, Any]:
        """Testa sintaxe dos arquivos Lua"""
        syntax_result = {
            "passed": True,
            "errors": [],
            "files_tested": 0,
            "files_with_errors": 0
        }
        
        for file_path, file_analysis in variation["files"].items():
            if file_analysis["file_type"] == ".lua":
                syntax_result["files_tested"] += 1
                
                content = file_analysis.get("content", "")
                syntax_errors = self.check_lua_syntax(content)
                
                if syntax_errors:
                    syntax_result["files_with_errors"] += 1
                    syntax_result["errors"].extend(syntax_errors)
                    syntax_result["passed"] = False
        
        return syntax_result
    
    def check_lua_syntax(self, content: str) -> List[str]:
        """Verifica sintaxe Lua usando análise de padrões"""
        errors = []
        
        lines = content.splitlines()
        
        # Verificar parênteses balanceados
        open_parens = 0
        close_parens = 0
        
        # Verificar chaves balanceadas
        open_braces = 0
        close_braces = 0
        
        # Verificar 'end' balanceados
        function_count = 0
        end_count = 0
        
        for i, line in enumerate(lines, 1):
            stripped_line = line.strip()
            
            # Contar parênteses
            open_parens += stripped_line.count('(')
            close_parens += stripped_line.count(')')
            
            # Contar chaves
            open_braces += stripped_line.count('{')
            close_braces += stripped_line.count('}')
            
            # Contar funções e ends
            if re.match(r'^function\s+', stripped_line):
                function_count += 1
            elif stripped_line == 'end':
                end_count += 1
        
        # Verificar desbalanceamentos
        if open_parens != close_parens:
            errors.append(f"Parênteses desbalanceados: {open_parens} abertos, {close_parens} fechados")
        
        if open_braces != close_braces:
            errors.append(f"Chaves desbalanceadas: {open_braces} abertas, {close_braces} fechadas")
        
        if function_count != end_count:
            errors.append(f"Funções e 'end' desbalanceados: {function_count} funções, {end_count} ends")
        
        # Verificar strings não fechadas
        if content.count('"') % 2 != 0:
            errors.append("String com aspas duplas não fechada")
        
        if content.count("'") % 2 != 0:
            errors.append("String com aspas simples não fechada")
        
        return errors
    
    def test_structure(self, variation: Dict[str, Any], 
                      original_analysis: Dict[str, Any]) -> Dict[str, Any]:
        """Testa estrutura da variação comparada com o original"""
        structure_result = {
            "passed": True,
            "warnings": [],
            "structure_changes": {},
            "missing_elements": [],
            "new_elements": []
        }
        
        # Comparar estrutura de arquivos
        original_files = set(original_analysis["files"].keys())
        variation_files = set(variation["files"].keys())
        
        # Arquivos faltando
        missing_files = original_files - variation_files
        if missing_files:
            structure_result["missing_elements"].extend(list(missing_files))
            structure_result["passed"] = False
        
        # Novos arquivos
        new_files = variation_files - original_files
        if new_files:
            structure_result["new_elements"].extend(list(new_files))
        
        # Comparar estrutura interna dos arquivos
        for file_path in original_files & variation_files:
            original_file = original_analysis["files"][file_path]
            variation_file = variation["files"][file_path]
            
            if original_file["file_type"] == ".lua":
                structure_changes = self.compare_lua_structure(original_file, variation_file)
                if structure_changes:
                    structure_result["structure_changes"][file_path] = structure_changes
        
        return structure_result
    
    def compare_lua_structure(self, original_file: Dict[str, Any], 
                            variation_file: Dict[str, Any]) -> Dict[str, Any]:
        """Compara estrutura de arquivos Lua"""
        changes = {
            "functions_added": [],
            "functions_removed": [],
            "functions_modified": [],
            "variables_added": [],
            "variables_removed": []
        }
        
        original_content = original_file.get("content", "")
        variation_content = variation_file.get("content", "")
        
        # Extrair funções
        original_functions = set(re.findall(r'function\s+(\w+)', original_content))
        variation_functions = set(re.findall(r'function\s+(\w+)', variation_content))
        
        changes["functions_added"] = list(variation_functions - original_functions)
        changes["functions_removed"] = list(original_functions - variation_functions)
        changes["functions_modified"] = list(original_functions & variation_functions)
        
        # Extrair variáveis locais
        original_vars = set(re.findall(r'local\s+(\w+)', original_content))
        variation_vars = set(re.findall(r'local\s+(\w+)', variation_content))
        
        changes["variables_added"] = list(variation_vars - original_vars)
        changes["variables_removed"] = list(original_vars - variation_vars)
        
        return changes
    
    def test_dependencies(self, variation: Dict[str, Any]) -> Dict[str, Any]:
        """Testa dependências da variação"""
        dependency_result = {
            "passed": True,
            "errors": [],
            "warnings": [],
            "missing_deps": [],
            "unused_deps": []
        }
        
        for file_path, file_analysis in variation["files"].items():
            if file_analysis["file_type"] == ".lua":
                content = file_analysis.get("content", "")
                
                # Verificar requires
                requires = re.findall(r'require\s*\([\'"]([^\'"]+)[\'"]\)', content)
                
                for req in requires:
                    # Verificar se o módulo existe
                    if not self.check_module_exists(req):
                        dependency_result["missing_deps"].append(req)
                        dependency_result["passed"] = False
                
                # Verificar APIs OTClient
                api_calls = re.findall(r'g_(\w+)\.', content)
                for api in api_calls:
                    if not self.check_api_exists(api):
                        dependency_result["warnings"].append(f"API g_{api} pode não existir")
        
        return dependency_result
    
    def check_module_exists(self, module_name: str) -> bool:
        """Verifica se um módulo existe"""
        module_path = os.path.join(self.modules_path, module_name)
        return os.path.exists(module_path)
    
    def check_api_exists(self, api_name: str) -> bool:
        """Verifica se uma API OTClient existe (simulado)"""
        # Lista de APIs conhecidas (simulada)
        known_apis = [
            "game", "ui", "sounds", "graphics", "app", "settings",
            "network", "resources", "input", "window", "console"
        ]
        return api_name in known_apis
    
    def test_compatibility(self, variation: Dict[str, Any], 
                         original_analysis: Dict[str, Any]) -> Dict[str, Any]:
        """Testa compatibilidade da variação"""
        compatibility_result = {
            "passed": True,
            "score": 0.0,
            "issues": [],
            "compatibility_notes": []
        }
        
        # Comparar com módulo original
        original_score = variation.get("compatibility_score", 0.0)
        compatibility_result["score"] = original_score
        
        if original_score < 0.7:
            compatibility_result["passed"] = False
            compatibility_result["issues"].append("Score de compatibilidade baixo")
        
        # Verificar modificações excessivas
        modifications = variation.get("modifications", {})
        total_mods = sum(modifications.values())
        
        if total_mods > 15:
            compatibility_result["issues"].append("Muitas modificações podem afetar compatibilidade")
            compatibility_result["passed"] = False
        
        # Verificar estrutura de arquivos
        if len(variation["files"]) != len(original_analysis["files"]):
            compatibility_result["issues"].append("Número de arquivos diferente do original")
            compatibility_result["passed"] = False
        
        return compatibility_result
    
    def test_performance(self, variation: Dict[str, Any]) -> Dict[str, Any]:
        """Testa performance da variação"""
        performance_result = {
            "passed": True,
            "score": 0.0,
            "issues": [],
            "metrics": {}
        }
        
        total_lines = 0
        total_functions = 0
        total_variables = 0
        
        for file_path, file_analysis in variation["files"].items():
            if file_analysis["file_type"] == ".lua":
                content = file_analysis.get("content", "")
                
                lines = len(content.splitlines())
                functions = len(re.findall(r'function\s+', content))
                variables = len(re.findall(r'local\s+', content))
                
                total_lines += lines
                total_functions += functions
                total_variables += variables
        
        performance_result["metrics"] = {
            "total_lines": total_lines,
            "total_functions": total_functions,
            "total_variables": total_variables,
            "complexity_ratio": total_functions / max(total_lines, 1)
        }
        
        # Avaliar performance baseada em métricas
        if total_lines > 1000:
            performance_result["issues"].append("Módulo muito grande pode afetar performance")
            performance_result["passed"] = False
        
        if performance_result["metrics"]["complexity_ratio"] > 0.1:
            performance_result["issues"].append("Alta complexidade pode afetar performance")
            performance_result["passed"] = False
        
        # Calcular score de performance
        performance_result["score"] = self.calculate_performance_score_from_metrics(performance_result["metrics"])
        
        return performance_result
    
    def test_security(self, variation: Dict[str, Any]) -> Dict[str, Any]:
        """Testa segurança da variação"""
        security_result = {
            "passed": True,
            "score": 0.0,
            "issues": [],
            "vulnerabilities": []
        }
        
        for file_path, file_analysis in variation["files"].items():
            if file_analysis["file_type"] == ".lua":
                content = file_analysis.get("content", "")
                
                # Verificar padrões inseguros
                security_issues = self.check_security_patterns(content)
                if security_issues:
                    security_result["vulnerabilities"].extend(security_issues)
                    security_result["passed"] = False
        
        # Calcular score de segurança
        security_result["score"] = self.calculate_security_score(security_result["vulnerabilities"])
        
        return security_result
    
    def check_security_patterns(self, content: str) -> List[str]:
        """Verifica padrões de segurança no código"""
        vulnerabilities = []
        
        # Padrões inseguros
        dangerous_patterns = [
            (r'loadstring\s*\(', "Uso de loadstring pode ser inseguro"),
            (r'dofile\s*\(', "Uso de dofile pode ser inseguro"),
            (r'load\s*\(', "Uso de load pode ser inseguro"),
            (r'os\.execute\s*\(', "Execução de comandos do sistema"),
            (r'io\.open\s*\(', "Acesso direto ao sistema de arquivos"),
            (r'debug\.', "Uso de funções de debug"),
            (r'collectgarbage\s*\(', "Controle manual de garbage collection")
        ]
        
        for pattern, description in dangerous_patterns:
            if re.search(pattern, content):
                vulnerabilities.append(description)
        
        return vulnerabilities
    
    def collect_errors(self, test_results: Dict[str, Any]) -> List[str]:
        """Coleta todos os erros dos testes"""
        errors = []
        
        for test_name, result in test_results.items():
            if not result.get("passed", True):
                errors.extend(result.get("errors", []))
        
        return errors
    
    def collect_warnings(self, test_results: Dict[str, Any]) -> List[str]:
        """Coleta todos os avisos dos testes"""
        warnings = []
        
        for test_name, result in test_results.items():
            warnings.extend(result.get("warnings", []))
        
        return warnings
    
    def calculate_quality_score(self, variation_result: Dict[str, Any]) -> float:
        """Calcula score de qualidade da variação"""
        score = 1.0
        
        # Penalizar erros
        error_count = len(variation_result["errors"])
        score -= error_count * 0.2
        
        # Penalizar avisos
        warning_count = len(variation_result["warnings"])
        score -= warning_count * 0.05
        
        # Bonus para testes que passaram
        passed_tests = sum(1 for result in variation_result["test_results"].values() 
                          if result.get("passed", False))
        total_tests = len(variation_result["test_results"])
        
        if total_tests > 0:
            score += (passed_tests / total_tests) * 0.3
        
        return max(0.0, min(1.0, score))
    
    def calculate_compatibility_score(self, variation_result: Dict[str, Any]) -> float:
        """Calcula score de compatibilidade"""
        compatibility_test = variation_result["test_results"].get("compatibility", {})
        return compatibility_test.get("score", 0.0)
    
    def calculate_performance_score(self, variation_result: Dict[str, Any]) -> float:
        """Calcula score de performance"""
        performance_test = variation_result["test_results"].get("performance", {})
        return performance_test.get("score", 0.0)
    
    def calculate_performance_score_from_metrics(self, metrics: Dict[str, Any]) -> float:
        """Calcula score de performance baseado em métricas"""
        score = 1.0
        
        # Penalizar módulos muito grandes
        if metrics["total_lines"] > 1000:
            score -= 0.3
        elif metrics["total_lines"] > 500:
            score -= 0.1
        
        # Penalizar alta complexidade
        if metrics["complexity_ratio"] > 0.1:
            score -= 0.2
        elif metrics["complexity_ratio"] > 0.05:
            score -= 0.1
        
        return max(0.0, min(1.0, score))
    
    def calculate_security_score(self, vulnerabilities: List[str]) -> float:
        """Calcula score de segurança"""
        score = 1.0
        
        # Penalizar vulnerabilidades
        score -= len(vulnerabilities) * 0.2
        
        return max(0.0, min(1.0, score))
    
    def generate_test_summary(self, variation_results: List[Dict[str, Any]]) -> Dict[str, Any]:
        """Gera resumo dos testes"""
        summary = {
            "total_variations": len(variation_results),
            "passed_variations": 0,
            "failed_variations": 0,
            "average_quality_score": 0.0,
            "average_compatibility_score": 0.0,
            "average_performance_score": 0.0,
            "total_errors": 0,
            "total_warnings": 0,
            "best_variation": None,
            "worst_variation": None
        }
        
        quality_scores = []
        compatibility_scores = []
        performance_scores = []
        
        for result in variation_results:
            # Contar variações que passaram
            if result["quality_score"] >= 0.7:
                summary["passed_variations"] += 1
            else:
                summary["failed_variations"] += 1
            
            # Coletar scores
            quality_scores.append(result["quality_score"])
            compatibility_scores.append(result["compatibility_score"])
            performance_scores.append(result["performance_score"])
            
            # Contar erros e avisos
            summary["total_errors"] += len(result["errors"])
            summary["total_warnings"] += len(result["warnings"])
        
        # Calcular médias
        if quality_scores:
            summary["average_quality_score"] = sum(quality_scores) / len(quality_scores)
        if compatibility_scores:
            summary["average_compatibility_score"] = sum(compatibility_scores) / len(compatibility_scores)
        if performance_scores:
            summary["average_performance_score"] = sum(performance_scores) / len(performance_scores)
        
        # Encontrar melhor e pior variação
        if variation_results:
            best_idx = max(range(len(variation_results)), 
                          key=lambda i: variation_results[i]["quality_score"])
            worst_idx = min(range(len(variation_results)), 
                           key=lambda i: variation_results[i]["quality_score"])
            
            summary["best_variation"] = variation_results[best_idx]["variation_name"]
            summary["worst_variation"] = variation_results[worst_idx]["variation_name"]
        
        return summary
    
    def generate_recommendations(self, test_report: Dict[str, Any]) -> List[str]:
        """Gera recomendações baseadas nos resultados dos testes"""
        recommendations = []
        
        summary = test_report["summary"]
        
        if summary["failed_variations"] > summary["passed_variations"]:
            recommendations.append("A maioria das variações falhou nos testes. Revisar critérios de geração.")
        
        if summary["average_quality_score"] < 0.7:
            recommendations.append("Score de qualidade baixo. Melhorar validação de sintaxe e estrutura.")
        
        if summary["average_compatibility_score"] < 0.8:
            recommendations.append("Score de compatibilidade baixo. Reduzir modificações estruturais.")
        
        if summary["total_errors"] > 0:
            recommendations.append(f"Encontrados {summary['total_errors']} erros. Corrigir problemas de sintaxe.")
        
        if summary["total_warnings"] > 10:
            recommendations.append("Muitos avisos. Revisar padrões de código e dependências.")
        
        if not recommendations:
            recommendations.append("Todas as variações passaram nos testes com boa qualidade.")
        
        return recommendations
    
    def save_test_report(self, module_name: str, test_report: Dict[str, Any]):
        """Salva relatório de testes"""
        output_file = os.path.join(
            self.results_path, 
            "test_reports", 
            f"{module_name}_test_report.json"
        )
        
        try:
            with open(output_file, 'w', encoding='utf-8') as f:
                json.dump(test_report, f, indent=2, ensure_ascii=False)
            print(f"✅ Relatório de testes salvo em: {output_file}")
        except Exception as e:
            print(f"⚠️ Erro ao salvar relatório de testes: {e}")

def main():
    """Função principal para teste do agente"""
    tester = ModuleTesterAgent()
    
    # Exemplo de variações (simulado)
    variations = [
        {
            "variation_name": "client_enhanced_1",
            "variation_id": 1,
            "files": {
                "client.lua": {
                    "content": "function init()\n  print('Hello')\nend",
                    "file_type": ".lua"
                }
            },
            "compatibility_score": 0.8,
            "modifications": {"total_files_modified": 1}
        }
    ]
    
    original_analysis = {
        "module_name": "client",
        "files": {
            "client.lua": {
                "content": "function init()\n  print('Hello')\nend",
                "file_type": ".lua"
            }
        }
    }
    
    # Testar variações
    test_report = tester.test_module_variations(variations, original_analysis)
    
    print(f"✅ Teste concluído")
    print(f"📊 Resumo: {test_report['summary']}")

if __name__ == "__main__":
    main() 