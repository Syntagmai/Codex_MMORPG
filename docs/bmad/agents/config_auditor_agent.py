#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Configuration Auditor Agent
Responsável por auditar regras e configurações do sistema
"""

import os
import json
import re
from datetime import datetime
from pathlib import Path
from typing import Dict, List, Set, Tuple
import argparse

class ConfigurationAuditor:
    def __init__(self, project_root: str = "."):
        self.project_root = Path(project_root).resolve()
        self.audit_results = {
            "timestamp": datetime.now().isoformat(),
            "project_root": str(self.project_root),
            "config_files": [],
            "rules_files": [],
            "issues": [],
            "obsolete_configs": [],
            "inconsistent_params": [],
            "missing_configs": [],
            "recommendations": []
        }
        
    def scan_configurations(self) -> Dict:
        """Escaneia todas as configurações e regras do sistema"""
        print("🔍 Iniciando auditoria de configurações e regras...")
        
        # Tipos de arquivos de configuração
        config_patterns = [
            "*.json", "*.yml", "*.yaml", "*.toml", "*.ini", "*.cfg", 
            "*.conf", "*.config", "*.properties", "*.env", "*.env.*"
        ]
        
        # Tipos de arquivos de regras
        rules_patterns = [
            "*.md", "*.txt", "*.rst", "*.rules", "*.policy"
        ]
        
        # Encontra arquivos de configuração
        for pattern in config_patterns:
            config_files = list(self.project_root.rglob(pattern))
            for config_file in config_files:
                if self._is_config_file(config_file):
                    self.audit_results["config_files"].append(str(config_file.relative_to(self.project_root)))
                    self._analyze_config_file(config_file)
        
        # Encontra arquivos de regras
        for pattern in rules_patterns:
            rules_files = list(self.project_root.rglob(pattern))
            for rules_file in rules_files:
                if self._is_rules_file(rules_file):
                    self.audit_results["rules_files"].append(str(rules_file.relative_to(self.project_root)))
                    self._analyze_rules_file(rules_file)
        
        # Análises específicas
        self._analyze_task_master_rules()
        self._analyze_bmad_configurations()
        self._analyze_project_structure_rules()
        self._generate_recommendations()
        
        return self.audit_results
    
    def _is_config_file(self, file_path: Path) -> bool:
        """Verifica se é um arquivo de configuração relevante"""
        # Exclui arquivos em diretórios que não são configurações
        exclude_patterns = [
            ".git", ".venv", "node_modules", "__pycache__", 
            "build", "dist", "target", "bin", "obj"
        ]
        
        for pattern in exclude_patterns:
            if pattern in str(file_path):
                return False
        
        return True
    
    def _is_rules_file(self, file_path: Path) -> bool:
        """Verifica se é um arquivo de regras relevante"""
        # Foca em arquivos que contêm regras do projeto
        relevant_patterns = [
            "task_master", "rules", "policy", "guidelines", 
            "standards", "conventions", "README", "CONTRIBUTING"
        ]
        
        file_name = file_path.name.lower()
        for pattern in relevant_patterns:
            if pattern in file_name:
                return True
        
        return False
    
    def _analyze_config_file(self, file_path: Path):
        """Analisa um arquivo de configuração"""
        relative_path = file_path.relative_to(self.project_root)
        
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # Verifica extensão e analisa adequadamente
            if file_path.suffix.lower() == '.json':
                self._analyze_json_config(content, relative_path)
            elif file_path.suffix.lower() in ['.yml', '.yaml']:
                self._analyze_yaml_config(content, relative_path)
            elif file_path.suffix.lower() == '.toml':
                self._analyze_toml_config(content, relative_path)
            else:
                self._analyze_generic_config(content, relative_path)
                
        except Exception as e:
            self.audit_results["issues"].append({
                "file": str(relative_path),
                "type": "config_read_error",
                "error": str(e),
                "severity": "medium"
            })
    
    def _analyze_json_config(self, content: str, file_path: Path):
        """Analisa arquivo JSON de configuração"""
        try:
            config = json.loads(content)
            self._check_config_values(config, str(file_path))
        except json.JSONDecodeError as e:
            self.audit_results["issues"].append({
                "file": str(file_path),
                "type": "json_syntax_error",
                "error": str(e),
                "severity": "high"
            })
    
    def _analyze_yaml_config(self, content: str, file_path: Path):
        """Analisa arquivo YAML de configuração"""
        # Verifica padrões comuns em YAML
        yaml_patterns = [
            r'^\s*[a-zA-Z_][a-zA-Z0-9_]*\s*:',  # Chaves
            r'^\s*-\s*',  # Listas
            r'^\s*#',  # Comentários
        ]
        
        for pattern in yaml_patterns:
            if not re.search(pattern, content, re.MULTILINE):
                self.audit_results["issues"].append({
                    "file": str(file_path),
                    "type": "yaml_format_issue",
                    "pattern": pattern,
                    "severity": "low"
                })
    
    def _analyze_toml_config(self, content: str, file_path: Path):
        """Analisa arquivo TOML de configuração"""
        # Verifica padrões TOML
        toml_patterns = [
            r'^\s*\[.*\]',  # Seções
            r'^\s*[a-zA-Z_][a-zA-Z0-9_]*\s*=',  # Chaves
        ]
        
        for pattern in toml_patterns:
            if not re.search(pattern, content, re.MULTILINE):
                self.audit_results["issues"].append({
                    "file": str(file_path),
                    "type": "toml_format_issue",
                    "pattern": pattern,
                    "severity": "low"
                })
    
    def _analyze_generic_config(self, content: str, file_path: Path):
        """Analisa arquivo de configuração genérico"""
        # Verifica padrões comuns
        config_patterns = [
            r'^\s*[a-zA-Z_][a-zA-Z0-9_]*\s*[=:]\s*',  # Chave-valor
            r'^\s*#',  # Comentários
        ]
        
        for pattern in config_patterns:
            if not re.search(pattern, content, re.MULTILINE):
                self.audit_results["issues"].append({
                    "file": str(file_path),
                    "type": "generic_config_issue",
                    "pattern": pattern,
                    "severity": "low"
                })
    
    def _check_config_values(self, config: Dict, file_path: str):
        """Verifica valores de configuração"""
        # Verifica valores obsoletos ou problemáticos
        obsolete_values = {
            "debug": True,
            "development": True,
            "test": True,
            "temp": True,
            "legacy": True
        }
        
        def check_dict(d, path=""):
            for key, value in d.items():
                current_path = f"{path}.{key}" if path else key
                
                # Verifica chaves obsoletas
                if key.lower() in obsolete_values:
                    self.audit_results["obsolete_configs"].append({
                        "file": file_path,
                        "path": current_path,
                        "value": value,
                        "reason": f"Chave obsoleta: {key}",
                        "severity": "medium"
                    })
                
                # Verifica valores problemáticos
                if isinstance(value, str) and value.lower() in ["true", "false"]:
                    # Possível inconsistência de tipo
                    self.audit_results["inconsistent_params"].append({
                        "file": file_path,
                        "path": current_path,
                        "value": value,
                        "issue": "String booleana em vez de boolean",
                        "severity": "low"
                    })
                
                # Recursão para dicionários aninhados
                if isinstance(value, dict):
                    check_dict(value, current_path)
        
        check_dict(config)
    
    def _analyze_rules_file(self, file_path: Path):
        """Analisa um arquivo de regras"""
        relative_path = file_path.relative_to(self.project_root)
        
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # Verifica padrões de regras
            rules_patterns = [
                r'##\s*Regras',  # Seções de regras
                r'###\s*',  # Subseções
                r'-\s*\[.*\]',  # Listas de tarefas
                r'✅|❌|⏳',  # Status indicators
            ]
            
            for pattern in rules_patterns:
                if not re.search(pattern, content, re.MULTILINE):
                    self.audit_results["issues"].append({
                        "file": str(relative_path),
                        "type": "rules_format_issue",
                        "pattern": pattern,
                        "severity": "low"
                    })
                    
        except Exception as e:
            self.audit_results["issues"].append({
                "file": str(relative_path),
                "type": "rules_read_error",
                "error": str(e),
                "severity": "medium"
            })
    
    def _analyze_task_master_rules(self):
        """Analisa regras específicas do Task Master"""
        task_master_file = self.project_root / "wiki" / "dashboard" / "task_master.md"
        
        if task_master_file.exists():
            try:
                with open(task_master_file, 'r', encoding='utf-8') as f:
                    content = f.read()
                
                # Verifica regras críticas
                critical_rules = [
                    "PRIORIDADE CRÍTICA",
                    "Regras Críticas",
                    "Critérios de Qualidade"
                ]
                
                for rule in critical_rules:
                    if rule not in content:
                        self.audit_results["missing_configs"].append({
                            "file": "wiki/dashboard/task_master.md",
                            "missing": rule,
                            "severity": "high"
                        })
                        
            except Exception as e:
                self.audit_results["issues"].append({
                    "file": "wiki/dashboard/task_master.md",
                    "type": "task_master_read_error",
                    "error": str(e),
                    "severity": "high"
                })
    
    def _analyze_bmad_configurations(self):
        """Analisa configurações específicas do BMAD"""
        bmad_dir = self.project_root / "wiki" / "bmad"
        
        if bmad_dir.exists():
            # Verifica arquivos de configuração BMAD
            bmad_configs = list(bmad_dir.rglob("*.py"))
            
            for config_file in bmad_configs:
                if "config" in config_file.name.lower():
                    self.audit_results["config_files"].append(str(config_file.relative_to(self.project_root)))
    
    def _analyze_project_structure_rules(self):
        """Analisa regras de estrutura do projeto"""
        # Verifica se existe .gitignore
        gitignore_file = self.project_root / ".gitignore"
        if not gitignore_file.exists():
            self.audit_results["missing_configs"].append({
                "file": ".gitignore",
                "missing": "Arquivo .gitignore",
                "severity": "medium"
            })
        
        # Verifica se existe README.md
        readme_file = self.project_root / "README.md"
        if not readme_file.exists():
            self.audit_results["missing_configs"].append({
                "file": "README.md",
                "missing": "Arquivo README.md",
                "severity": "high"
            })
    
    def _generate_recommendations(self):
        """Gera recomendações baseadas na análise"""
        recommendations = []
        
        # Recomendações baseadas em problemas encontrados
        if self.audit_results["obsolete_configs"]:
            recommendations.append({
                "category": "Limpeza",
                "action": "Remover configurações obsoletas",
                "priority": "medium",
                "description": f"Encontradas {len(self.audit_results['obsolete_configs'])} configurações obsoletas"
            })
        
        if self.audit_results["inconsistent_params"]:
            recommendations.append({
                "category": "Padronização",
                "action": "Padronizar parâmetros de configuração",
                "priority": "low",
                "description": f"Encontrados {len(self.audit_results['inconsistent_params'])} parâmetros inconsistentes"
            })
        
        if self.audit_results["missing_configs"]:
            recommendations.append({
                "category": "Completude",
                "action": "Criar configurações faltantes",
                "priority": "high",
                "description": f"Encontradas {len(self.audit_results['missing_configs'])} configurações faltantes"
            })
        
        # Recomendações gerais
        recommendations.extend([
            {
                "category": "Documentação",
                "action": "Documentar todas as configurações",
                "priority": "medium",
                "description": "Para melhor manutenibilidade"
            },
            {
                "category": "Validação",
                "action": "Implementar validação de configurações",
                "priority": "medium",
                "description": "Para evitar erros de configuração"
            },
            {
                "category": "Versionamento",
                "action": "Versionar configurações",
                "priority": "low",
                "description": "Para controle de mudanças"
            }
        ])
        
        self.audit_results["recommendations"] = recommendations
    
    def save_report(self, output_file: str = "config_audit_report.json"):
        """Salva o relatório em arquivo JSON"""
        output_path = Path(output_file)
        output_path.parent.mkdir(parents=True, exist_ok=True)
        
        with open(output_path, 'w', encoding='utf-8') as f:
            json.dump(self.audit_results, f, indent=2, ensure_ascii=False)
        
        print(f"📄 Relatório salvo em: {output_path}")
        return output_path
    
    def print_summary(self):
        """Imprime resumo da auditoria"""
        print("\n" + "="*60)
        print("📊 RESUMO DA AUDITORIA DE CONFIGURAÇÕES")
        print("="*60)
        
        print(f"⚙️  Arquivos de configuração: {len(self.audit_results['config_files'])}")
        print(f"📋 Arquivos de regras: {len(self.audit_results['rules_files'])}")
        print(f"⚠️  Problemas encontrados: {len(self.audit_results['issues'])}")
        print(f"🗑️  Configurações obsoletas: {len(self.audit_results['obsolete_configs'])}")
        print(f"🔧 Parâmetros inconsistentes: {len(self.audit_results['inconsistent_params'])}")
        print(f"❌ Configurações faltantes: {len(self.audit_results['missing_configs'])}")
        print(f"💡 Recomendações: {len(self.audit_results['recommendations'])}")
        
        # Mostra configurações obsoletas
        if self.audit_results['obsolete_configs']:
            print(f"\n🗑️  CONFIGURAÇÕES OBSOLETAS:")
            for config in self.audit_results['obsolete_configs'][:5]:
                print(f"  • {config['file']}: {config['path']} - {config['reason']}")
        
        # Mostra configurações faltantes
        if self.audit_results['missing_configs']:
            print(f"\n❌ CONFIGURAÇÕES FALTANTES:")
            for config in self.audit_results['missing_configs'][:5]:
                print(f"  • {config['file']}: {config['missing']}")
        
        print("\n" + "="*60)

def main():
    parser = argparse.ArgumentParser(description="Configuration Auditor Agent")
    parser.add_argument("--project-root", default=".", help="Raiz do projeto para auditar")
    parser.add_argument("--output", default="config_audit_report.json", help="Arquivo de saída")
    parser.add_argument("--scan", action="store_true", help="Executar escaneamento completo")
    
    args = parser.parse_args()
    
    if args.scan:
        auditor = ConfigurationAuditor(args.project_root)
        results = auditor.scan_configurations()
        auditor.save_report(args.output)
        auditor.print_summary()
        
        return results
    
    print("🔍 Configuration Auditor Agent")
    print("Use --scan para executar a auditoria completa")

if __name__ == "__main__":
    main() 