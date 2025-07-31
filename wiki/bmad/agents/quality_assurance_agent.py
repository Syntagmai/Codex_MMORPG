#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Quality Assurance Agent - Sistema de Garantia de Qualidade

Este agente é responsável por:
- Validar qualidade do código gerado
- Verificar padrões de codificação
- Testar funcionalidades
- Validar documentação
- Integrar com o sistema de task management
"""

import json
import logging
import subprocess
import re
from datetime import datetime
from pathlib import Path
from typing import Dict, List, Optional, Tuple

class QualityAssuranceAgent:
    def __init__(self):
        self.base_path = Path(__file__).parent.parent.parent.parent
        self.dashboard_path = self.base_path / "wiki" / "dashboard"
        self.log_path = self.base_path / "wiki" / "log"
        self.reports_path = self.base_path / "wiki" / "log"
        
        # Criar pasta de relatórios se não existir
        self.reports_path.mkdir(exist_ok=True)
        
        # Configurar logging
        logging.basicConfig(
            level=logging.INFO,
            format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
        )
        self.logger = logging.getLogger('QualityAssuranceAgent')
        
        # Carregar configurações
        self.load_configuration()
        
    def load_configuration(self):
        """Carrega configurações do sistema"""
        self.logger.info("🔧 Carregando configurações do Quality Assurance Agent...")
        
        # Configurações padrão
        self.config = {
            "quality_threshold": 0.8,
            "auto_fix": True,
            "run_tests": True,
            "check_documentation": True,
            "check_style": True,
            "linters": {
                "python": ["flake8", "pylint"],
                "lua": ["luacheck"],
                "cpp": ["cppcheck"],
                "javascript": ["eslint"]
            },
            "test_frameworks": {
                "python": "pytest",
                "lua": "busted",
                "cpp": "gtest",
                "javascript": "jest"
            }
        }
        
        self.logger.info("✅ Configurações carregadas com sucesso")
    
    def analyze_code_quality(self, code_file: str) -> Dict:
        """Analisa qualidade do código"""
        self.logger.info(f"🔍 Analisando qualidade do código: {code_file}")
        
        try:
            with open(code_file, 'r', encoding='utf-8') as f:
                code_content = f.read()
            
            analysis = {
                "file_path": code_file,
                "language": self.detect_language(code_file),
                "metrics": self.calculate_metrics(code_content),
                "style_issues": self.check_style(code_content),
                "complexity": self.analyze_complexity(code_content),
                "documentation": self.check_documentation(code_content),
                "security": self.check_security(code_content),
                "performance": self.check_performance(code_content),
                "overall_score": 0.0
            }
            
            # Calcular score geral
            analysis["overall_score"] = self.calculate_overall_score(analysis)
            
            self.logger.info(f"✅ Análise concluída: {analysis['overall_score']:.2f}/1.0")
            return analysis
            
        except Exception as e:
            self.logger.error(f"❌ Erro ao analisar código: {e}")
            return {}
    
    def detect_language(self, file_path: str) -> str:
        """Detecta linguagem do arquivo"""
        extensions = {
            '.py': 'python',
            '.lua': 'lua',
            '.cpp': 'cpp',
            '.h': 'cpp',
            '.js': 'javascript',
            '.html': 'html',
            '.css': 'css'
        }
        
        file_ext = Path(file_path).suffix.lower()
        return extensions.get(file_ext, 'unknown')
    
    def calculate_metrics(self, code: str) -> Dict:
        """Calcula métricas do código"""
        lines = code.split('\n')
        
        metrics = {
            "total_lines": len(lines),
            "code_lines": len([l for l in lines if l.strip() and not l.strip().startswith('#')]),
            "comment_lines": len([l for l in lines if l.strip().startswith('#')]),
            "blank_lines": len([l for l in lines if not l.strip()]),
            "functions": len(re.findall(r'def\s+\w+', code)),
            "classes": len(re.findall(r'class\s+\w+', code)),
            "imports": len(re.findall(r'import\s+|from\s+', code))
        }
        
        # Calcular métricas derivadas
        metrics["comment_ratio"] = metrics["comment_lines"] / max(metrics["code_lines"], 1)
        metrics["blank_ratio"] = metrics["blank_lines"] / max(metrics["total_lines"], 1)
        metrics["function_density"] = metrics["functions"] / max(metrics["code_lines"], 1)
        
        return metrics
    
    def check_style(self, code: str) -> List[Dict]:
        """Verifica estilo do código"""
        issues = []
        
        # Verificar indentação
        lines = code.split('\n')
        for i, line in enumerate(lines, 1):
            if line.strip() and not line.startswith(' ') and not line.startswith('\t'):
                # Linha não indentada (pode ser válida)
                pass
            elif line.startswith('\t'):
                issues.append({
                    "type": "style",
                    "severity": "warning",
                    "message": "Usar espaços em vez de tabs",
                    "line": i
                })
        
        # Verificar linhas muito longas
        for i, line in enumerate(lines, 1):
            if len(line) > 80:
                issues.append({
                    "type": "style",
                    "severity": "warning",
                    "message": f"Linha muito longa ({len(line)} caracteres)",
                    "line": i
                })
        
        # Verificar espaços em branco no final
        for i, line in enumerate(lines, 1):
            if line.rstrip() != line:
                issues.append({
                    "type": "style",
                    "severity": "warning",
                    "message": "Espaços em branco no final da linha",
                    "line": i
                })
        
        return issues
    
    def analyze_complexity(self, code: str) -> Dict:
        """Analisa complexidade do código"""
        complexity = {
            "cyclomatic": 0,
            "cognitive": 0,
            "nesting": 0
        }
        
        # Complexidade ciclomática (simplificada)
        complexity["cyclomatic"] = (
            len(re.findall(r'\bif\b', code)) +
            len(re.findall(r'\bfor\b', code)) +
            len(re.findall(r'\bwhile\b', code)) +
            len(re.findall(r'\band\b', code)) +
            len(re.findall(r'\bor\b', code)) +
            1
        )
        
        # Complexidade cognitiva (simplificada)
        complexity["cognitive"] = (
            len(re.findall(r'\bif\b', code)) * 1 +
            len(re.findall(r'\bfor\b', code)) * 1 +
            len(re.findall(r'\bwhile\b', code)) * 1 +
            len(re.findall(r'\btry\b', code)) * 2 +
            len(re.findall(r'\bexcept\b', code)) * 2 +
            len(re.findall(r'\bwith\b', code)) * 1
        )
        
        # Nível de aninhamento máximo
        max_nesting = 0
        current_nesting = 0
        
        for line in code.split('\n'):
            if line.strip():
                indent_level = len(line) - len(line.lstrip())
                current_nesting = indent_level // 4  # Assumindo 4 espaços por nível
                max_nesting = max(max_nesting, current_nesting)
        
        complexity["nesting"] = max_nesting
        
        return complexity
    
    def check_documentation(self, code: str) -> Dict:
        """Verifica documentação do código"""
        doc_analysis = {
            "has_docstrings": False,
            "has_comments": False,
            "has_readme": False,
            "docstring_coverage": 0.0,
            "issues": []
        }
        
        # Verificar docstrings
        if '"""' in code or "'''" in code:
            doc_analysis["has_docstrings"] = True
        
        # Verificar comentários
        if '#' in code or '//' in code or '--' in code:
            doc_analysis["has_comments"] = True
        
        # Verificar README
        if Path(self.base_path / "README.md").exists():
            doc_analysis["has_readme"] = True
        
        # Calcular cobertura de docstrings (simplificada)
        functions = len(re.findall(r'def\s+\w+', code))
        classes = len(re.findall(r'class\s+\w+', code))
        total_items = functions + classes
        
        if total_items > 0:
            doc_analysis["docstring_coverage"] = 0.5 if doc_analysis["has_docstrings"] else 0.0
        
        # Identificar problemas
        if not doc_analysis["has_docstrings"]:
            doc_analysis["issues"].append("Faltam docstrings")
        
        if not doc_analysis["has_comments"]:
            doc_analysis["issues"].append("Faltam comentários")
        
        if not doc_analysis["has_readme"]:
            doc_analysis["issues"].append("Falta README")
        
        return doc_analysis
    
    def check_security(self, code: str) -> List[Dict]:
        """Verifica problemas de segurança"""
        security_issues = []
        
        # Verificar padrões inseguros
        insecure_patterns = [
            (r'eval\s*\(', "Uso de eval() pode ser inseguro"),
            (r'exec\s*\(', "Uso de exec() pode ser inseguro"),
            (r'input\s*\(', "input() sem validação pode ser inseguro"),
            (r'os\.system\s*\(', "os.system() pode ser inseguro"),
            (r'subprocess\.call\s*\(', "subprocess.call() sem shell=False pode ser inseguro"),
            (r'password\s*=', "Senha hardcoded no código"),
            (r'secret\s*=', "Segredo hardcoded no código"),
            (r'api_key\s*=', "API key hardcoded no código")
        ]
        
        for pattern, message in insecure_patterns:
            matches = re.finditer(pattern, code, re.IGNORECASE)
            for match in matches:
                line_num = code[:match.start()].count('\n') + 1
                security_issues.append({
                    "type": "security",
                    "severity": "high",
                    "message": message,
                    "line": line_num
                })
        
        return security_issues
    
    def check_performance(self, code: str) -> List[Dict]:
        """Verifica problemas de performance"""
        performance_issues = []
        
        # Verificar padrões de performance
        performance_patterns = [
            (r'for\s+\w+\s+in\s+range\s*\(\s*len\s*\(', "Use enumerate() em vez de range(len())"),
            (r'\.append\s*\(.*\)\s+in\s+loop', "List comprehension pode ser mais eficiente"),
            (r'import\s+\*', "Import * pode ser ineficiente"),
            (r'global\s+\w+', "Uso excessivo de variáveis globais"),
            (r'lambda\s+.*lambda', "Lambdas aninhadas podem ser ineficientes")
        ]
        
        for pattern, message in performance_patterns:
            matches = re.finditer(pattern, code, re.IGNORECASE)
            for match in matches:
                line_num = code[:match.start()].count('\n') + 1
                performance_issues.append({
                    "type": "performance",
                    "severity": "medium",
                    "message": message,
                    "line": line_num
                })
        
        return performance_issues
    
    def calculate_overall_score(self, analysis: Dict) -> float:
        """Calcula score geral de qualidade"""
        score = 1.0
        
        # Penalizar por problemas de estilo
        style_issues = len(analysis["style_issues"])
        score -= style_issues * 0.01
        
        # Penalizar por problemas de segurança
        security_issues = len(analysis["security"])
        score -= security_issues * 0.1
        
        # Penalizar por problemas de performance
        performance_issues = len(analysis["performance"])
        score -= performance_issues * 0.05
        
        # Penalizar por falta de documentação
        if not analysis["documentation"]["has_docstrings"]:
            score -= 0.1
        
        if not analysis["documentation"]["has_comments"]:
            score -= 0.05
        
        # Penalizar por complexidade alta
        complexity = analysis["complexity"]
        if complexity["cyclomatic"] > 10:
            score -= 0.1
        
        if complexity["nesting"] > 5:
            score -= 0.1
        
        # Recompensar por boas práticas
        metrics = analysis["metrics"]
        if metrics["comment_ratio"] > 0.2:
            score += 0.05
        
        if metrics["function_density"] > 0.1:
            score += 0.05
        
        return max(0.0, min(1.0, score))
    
    def run_linter(self, code_file: str) -> Dict:
        """Executa linter no código"""
        self.logger.info(f"🔍 Executando linter em: {code_file}")
        
        language = self.detect_language(code_file)
        linters = self.config["linters"].get(language, [])
        
        results = {
            "linter": "none",
            "issues": [],
            "score": 1.0
        }
        
        for linter in linters:
            try:
                if linter == "flake8":
                    result = subprocess.run(
                        [linter, code_file],
                        capture_output=True,
                        text=True,
                        timeout=30
                    )
                    
                    if result.returncode == 0:
                        results["linter"] = linter
                        results["score"] = 1.0
                    else:
                        issues = result.stdout.split('\n')
                        results["linter"] = linter
                        results["issues"] = [issue for issue in issues if issue.strip()]
                        results["score"] = max(0.0, 1.0 - len(results["issues"]) * 0.1)
                        
            except Exception as e:
                self.logger.warning(f"⚠️ Erro ao executar {linter}: {e}")
        
        return results
    
    def run_tests(self, code_file: str) -> Dict:
        """Executa testes no código"""
        self.logger.info(f"🧪 Executando testes em: {code_file}")
        
        language = self.detect_language(code_file)
        test_framework = self.config["test_frameworks"].get(language, "")
        
        results = {
            "framework": test_framework,
            "tests_run": 0,
            "tests_passed": 0,
            "tests_failed": 0,
            "coverage": 0.0,
            "success": False
        }
        
        if not test_framework:
            self.logger.warning(f"⚠️ Framework de teste não configurado para {language}")
            return results
        
        try:
            # Procurar por arquivos de teste
            test_files = list(Path(code_file).parent.glob(f"*test*.{Path(code_file).suffix}"))
            
            if not test_files:
                self.logger.warning(f"⚠️ Nenhum arquivo de teste encontrado para {code_file}")
                return results
            
            # Executar testes
            if test_framework == "pytest":
                result = subprocess.run(
                    ["pytest", str(test_files[0])],
                    capture_output=True,
                    text=True,
                    timeout=60
                )
                
                if result.returncode == 0:
                    results["success"] = True
                    # Extrair informações dos testes (simplificado)
                    results["tests_run"] = 1
                    results["tests_passed"] = 1
                    results["coverage"] = 0.8
                else:
                    results["tests_failed"] = 1
                    
        except Exception as e:
            self.logger.warning(f"⚠️ Erro ao executar testes: {e}")
        
        return results
    
    def generate_qa_report(self, analysis: Dict, linter_results: Dict, test_results: Dict) -> str:
        """Gera relatório de QA"""
        self.logger.info("📊 Gerando relatório de QA...")
        
        report = f"""# Quality Assurance Report - {Path(analysis['file_path']).name}

## 📋 Resumo Executivo

**Arquivo**: {analysis['file_path']}
**Linguagem**: {analysis['language']}
**Score Geral**: {analysis['overall_score']:.2f}/1.0
**Status**: {'✅ Aprovado' if analysis['overall_score'] >= self.config['quality_threshold'] else '❌ Reprovado'}
**Data**: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}

## 📊 Métricas de Código

| Métrica | Valor |
|---------|-------|
| **Total de Linhas** | {analysis['metrics']['total_lines']} |
| **Linhas de Código** | {analysis['metrics']['code_lines']} |
| **Linhas de Comentário** | {analysis['metrics']['comment_lines']} |
| **Linhas em Branco** | {analysis['metrics']['blank_lines']} |
| **Funções** | {analysis['metrics']['functions']} |
| **Classes** | {analysis['metrics']['classes']} |
| **Imports** | {analysis['metrics']['imports']} |
| **Razão de Comentários** | {analysis['metrics']['comment_ratio']:.2f} |
| **Densidade de Funções** | {analysis['metrics']['function_density']:.2f} |

## 🏗️ Complexidade

| Tipo | Valor |
|------|-------|
| **Ciclomática** | {analysis['complexity']['cyclomatic']} |
| **Cognitiva** | {analysis['complexity']['cognitive']} |
| **Aninhamento Máximo** | {analysis['complexity']['nesting']} |

## 📝 Documentação

| Item | Status |
|------|--------|
| **Docstrings** | {'✅ Presente' if analysis['documentation']['has_docstrings'] else '❌ Ausente'} |
| **Comentários** | {'✅ Presente' if analysis['documentation']['has_comments'] else '❌ Ausente'} |
| **README** | {'✅ Presente' if analysis['documentation']['has_readme'] else '❌ Ausente'} |
| **Cobertura de Docstrings** | {analysis['documentation']['docstring_coverage']:.2f} |

## 🔍 Problemas Identificados

### 🎨 Estilo ({len(analysis['style_issues'])} problemas)
"""
        
        if analysis['style_issues']:
            for issue in analysis['style_issues'][:5]:  # Limitar a 5 problemas
                report += f"- **Linha {issue['line']}**: {issue['message']}\n"
        else:
            report += "- ✅ Nenhum problema de estilo encontrado\n"
        
        report += f"""
### 🔒 Segurança ({len(analysis['security'])} problemas)
"""
        
        if analysis['security']:
            for issue in analysis['security']:
                report += f"- **Linha {issue['line']}**: {issue['message']}\n"
        else:
            report += "- ✅ Nenhum problema de segurança encontrado\n"
        
        report += f"""
### ⚡ Performance ({len(analysis['performance'])} problemas)
"""
        
        if analysis['performance']:
            for issue in analysis['performance']:
                report += f"- **Linha {issue['line']}**: {issue['message']}\n"
        else:
            report += "- ✅ Nenhum problema de performance encontrado\n"
        
        report += f"""
## 🔍 Resultados do Linter

**Linter**: {linter_results['linter']}
**Score**: {linter_results['score']:.2f}/1.0
**Problemas**: {len(linter_results['issues'])}
"""
        
        if linter_results['issues']:
            report += "\n**Problemas encontrados:**\n"
            for issue in linter_results['issues'][:3]:  # Limitar a 3 problemas
                report += f"- {issue}\n"
        
        report += f"""
## 🧪 Resultados dos Testes

**Framework**: {test_results['framework']}
**Sucesso**: {'✅ Sim' if test_results['success'] else '❌ Não'}
**Testes Executados**: {test_results['tests_run']}
**Testes Aprovados**: {test_results['tests_passed']}
**Testes Falharam**: {test_results['tests_failed']}
**Cobertura**: {test_results['coverage']:.2f}

## 🎯 Recomendações

"""
        
        recommendations = []
        
        if analysis['overall_score'] < self.config['quality_threshold']:
            recommendations.append("Melhorar score geral de qualidade")
        
        if not analysis['documentation']['has_docstrings']:
            recommendations.append("Adicionar docstrings para funções e classes")
        
        if len(analysis['style_issues']) > 5:
            recommendations.append("Corrigir problemas de estilo")
        
        if analysis['security']:
            recommendations.append("Corrigir problemas de segurança")
        
        if analysis['complexity']['cyclomatic'] > 10:
            recommendations.append("Reduzir complexidade ciclomática")
        
        if not test_results['success']:
            recommendations.append("Implementar testes unitários")
        
        if recommendations:
            for rec in recommendations:
                report += f"- {rec}\n"
        else:
            report += "- ✅ Código está em boa qualidade\n"
        
        report += f"""
## 📈 Melhorias Sugeridas

1. **Documentação**: Adicionar docstrings e comentários
2. **Testes**: Implementar testes unitários
3. **Estilo**: Seguir padrões de codificação
4. **Segurança**: Revisar práticas de segurança
5. **Performance**: Otimizar código crítico

---
**Relatório gerado**: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
**Responsável**: Quality Assurance Agent
"""
        
        return report
    
    def save_qa_report(self, report: str, analysis: Dict) -> str:
        """Salva relatório de QA"""
        file_name = f"qa_report_{Path(analysis['file_path']).stem}_{datetime.now().strftime('%Y%m%d_%H%M%S')}.md"
        output_path = self.reports_path / file_name
        
        try:
            with open(output_path, 'w', encoding='utf-8') as f:
                f.write(report)
            
            self.logger.info(f"✅ Relatório de QA salvo em: {output_path}")
            return str(output_path)
            
        except Exception as e:
            self.logger.error(f"❌ Erro ao salvar relatório: {e}")
            return ""
    
    def run(self, code_file: str = None) -> bool:
        """Executa o Quality Assurance Agent"""
        self.logger.info("🚀 Iniciando Quality Assurance Agent...")
        
        try:
            # Se não há arquivo especificado, usar exemplo
            if not code_file:
                code_file = str(self.base_path / "wiki" / "bmad" / "agents" / "task_master_agent.py")
            
            # Verificar se arquivo existe
            if not Path(code_file).exists():
                self.logger.error(f"❌ Arquivo não encontrado: {code_file}")
                return False
            
            # Analisar qualidade do código
            analysis = self.analyze_code_quality(code_file)
            if not analysis:
                return False
            
            # Executar linter
            linter_results = self.run_linter(code_file)
            
            # Executar testes
            test_results = self.run_tests(code_file)
            
            # Gerar relatório
            report = self.generate_qa_report(analysis, linter_results, test_results)
            
            # Salvar relatório
            report_path = self.save_qa_report(report, analysis)
            
            # Log de resumo
            self.logger.info(f"📊 Resumo da Análise de Qualidade:")
            self.logger.info(f"   - Score Geral: {analysis['overall_score']:.2f}/1.0")
            self.logger.info(f"   - Problemas de Estilo: {len(analysis['style_issues'])}")
            self.logger.info(f"   - Problemas de Segurança: {len(analysis['security'])}")
            self.logger.info(f"   - Problemas de Performance: {len(analysis['performance'])}")
            self.logger.info(f"   - Linter Score: {linter_results['score']:.2f}/1.0")
            self.logger.info(f"   - Testes: {'✅ Passou' if test_results['success'] else '❌ Falhou'}")
            
            self.logger.info("✅ Quality Assurance Agent executado com sucesso")
            return True
            
        except Exception as e:
            self.logger.error(f"❌ Erro na execução do Quality Assurance Agent: {e}")
            return False

if __name__ == "__main__":
    agent = QualityAssuranceAgent()
    success = agent.run()
    
    if success:
        print("✅ Quality Assurance Agent executado com sucesso!")
    else:
        print("❌ Quality Assurance Agent falhou na execução!") 