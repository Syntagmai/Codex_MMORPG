#!/usr/bin/env python3
"""
Security Auditor Agent - Epic 17 Task 17.7
Analisa segurança, validações, autenticação, permissões e vulnerabilidades
"""

import os
import json
import re
import hashlib
from datetime import datetime
from pathlib import Path

class SecurityAuditor:
    def __init__(self, project_root):
        self.project_root = Path(project_root)
        self.report = {
            "timestamp": datetime.now().isoformat(),
            "project_root": str(self.project_root),
            "security_issues": [],
            "authentication_issues": [],
            "permission_issues": [],
            "validation_issues": [],
            "vulnerabilities": [],
            "encryption_usage": [],
            "sensitive_data": [],
            "security_configs": [],
            "metrics": {}
        }
    
    def analyze_security_patterns(self):
        """Analisa padrões de segurança no código"""
        print("🔍 Analisando padrões de segurança...")
        
        security_patterns = {
            "sql_injection": [
                r"SELECT.*WHERE.*\$\{.*\}",
                r"INSERT.*VALUES.*\$\{.*\}",
                r"UPDATE.*SET.*\$\{.*\}",
                r"DELETE.*WHERE.*\$\{.*\}"
            ],
            "xss": [
                r"innerHTML\s*=\s*[^;]+",
                r"document\.write\s*\(\s*[^)]+\)",
                r"eval\s*\(\s*[^)]+\)"
            ],
            "path_traversal": [
                r"\.\./",
                r"\.\.\\",
                r"open\s*\(\s*[^)]*\.\./",
                r"readFile\s*\(\s*[^)]*\.\./"
            ],
            "hardcoded_credentials": [
                r"password\s*=\s*['\"][^'\"]+['\"]",
                r"secret\s*=\s*['\"][^'\"]+['\"]",
                r"api_key\s*=\s*['\"][^'\"]+['\"]",
                r"token\s*=\s*['\"][^'\"]+['\"]"
            ],
            "weak_encryption": [
                r"md5\s*\(",
                r"sha1\s*\(",
                r"base64\.",
                r"ROT13"
            ]
        }
        
        for root, dirs, files in os.walk(self.project_root):
            for file in files:
                if file.endswith(('.py', '.lua', '.js', '.php', '.java', '.cpp', '.hpp')):
                    file_path = Path(root) / file
                    try:
                        with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
                            content = f.read()
                        
                        for vuln_type, patterns in security_patterns.items():
                            for pattern in patterns:
                                matches = re.findall(pattern, content, re.IGNORECASE)
                                if matches:
                                    self.report["vulnerabilities"].append({
                                        "type": vuln_type,
                                        "file": str(file_path.relative_to(self.project_root)),
                                        "pattern": pattern,
                                        "matches": len(matches),
                                        "severity": "high" if vuln_type in ["sql_injection", "xss"] else "medium"
                                    })
                    except:
                        continue
    
    def analyze_authentication(self):
        """Analisa sistemas de autenticação"""
        print("🔍 Analisando autenticação...")
        
        auth_patterns = [
            r"login\s*\(",
            r"authenticate\s*\(",
            r"auth\s*\(",
            r"session\s*\[",
            r"cookie\s*\[",
            r"JWT",
            r"OAuth",
            r"password_hash",
            r"bcrypt",
            r"argon2"
        ]
        
        for root, dirs, files in os.walk(self.project_root):
            for file in files:
                if file.endswith(('.py', '.lua', '.js', '.php')):
                    file_path = Path(root) / file
                    try:
                        with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
                            content = f.read()
                        
                        for pattern in auth_patterns:
                            matches = re.findall(pattern, content, re.IGNORECASE)
                            if matches:
                                self.report["authentication_issues"].append({
                                    "file": str(file_path.relative_to(self.project_root)),
                                    "pattern": pattern,
                                    "matches": len(matches),
                                    "type": "authentication_method"
                                })
                    except:
                        continue
    
    def analyze_permissions(self):
        """Analisa sistemas de permissões"""
        print("🔍 Analisando permissões...")
        
        permission_patterns = [
            r"chmod\s*\(",
            r"chown\s*\(",
            r"permissions\s*\[",
            r"role\s*\[",
            r"admin\s*\[",
            r"sudo\s*\(",
            r"privilege",
            r"authorization",
            r"access_control"
        ]
        
        for root, dirs, files in os.walk(self.project_root):
            for file in files:
                if file.endswith(('.py', '.lua', '.js', '.sh', '.bat')):
                    file_path = Path(root) / file
                    try:
                        with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
                            content = f.read()
                        
                        for pattern in permission_patterns:
                            matches = re.findall(pattern, content, re.IGNORECASE)
                            if matches:
                                self.report["permission_issues"].append({
                                    "file": str(file_path.relative_to(self.project_root)),
                                    "pattern": pattern,
                                    "matches": len(matches),
                                    "type": "permission_check"
                                })
                    except:
                        continue
    
    def analyze_validations(self):
        """Analisa validações de entrada"""
        print("🔍 Analisando validações...")
        
        validation_patterns = [
            r"validate\s*\(",
            r"sanitize\s*\(",
            r"escape\s*\(",
            r"filter\s*\(",
            r"regex\s*\(",
            r"pattern\s*\(",
            r"input\s*validation",
            r"data\s*validation"
        ]
        
        for root, dirs, files in os.walk(self.project_root):
            for file in files:
                if file.endswith(('.py', '.lua', '.js', '.php')):
                    file_path = Path(root) / file
                    try:
                        with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
                            content = f.read()
                        
                        for pattern in validation_patterns:
                            matches = re.findall(pattern, content, re.IGNORECASE)
                            if matches:
                                self.report["validation_issues"].append({
                                    "file": str(file_path.relative_to(self.project_root)),
                                    "pattern": pattern,
                                    "matches": len(matches),
                                    "type": "validation_method"
                                })
                    except:
                        continue
    
    def analyze_encryption_usage(self):
        """Analisa uso de criptografia"""
        print("🔍 Analisando uso de criptografia...")
        
        encryption_patterns = [
            r"cryptography",
            r"pycryptodome",
            r"openssl",
            r"aes\s*\(",
            r"rsa\s*\(",
            r"sha256\s*\(",
            r"sha512\s*\(",
            r"bcrypt\s*\(",
            r"argon2\s*\(",
            r"encrypt\s*\(",
            r"decrypt\s*\("
        ]
        
        for root, dirs, files in os.walk(self.project_root):
            for file in files:
                if file.endswith(('.py', '.lua', '.js', '.cpp', '.hpp')):
                    file_path = Path(root) / file
                    try:
                        with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
                            content = f.read()
                        
                        for pattern in encryption_patterns:
                            matches = re.findall(pattern, content, re.IGNORECASE)
                            if matches:
                                self.report["encryption_usage"].append({
                                    "file": str(file_path.relative_to(self.project_root)),
                                    "pattern": pattern,
                                    "matches": len(matches),
                                    "type": "encryption_method"
                                })
                    except:
                        continue
    
    def analyze_sensitive_data(self):
        """Analisa dados sensíveis"""
        print("🔍 Analisando dados sensíveis...")
        
        sensitive_patterns = [
            r"password\s*=",
            r"secret\s*=",
            r"api_key\s*=",
            r"token\s*=",
            r"private_key\s*=",
            r"database_url\s*=",
            r"connection_string\s*=",
            r"admin\s*=",
            r"root\s*="
        ]
        
        for root, dirs, files in os.walk(self.project_root):
            for file in files:
                if file.endswith(('.py', '.lua', '.js', '.json', '.conf', '.config', '.env')):
                    file_path = Path(root) / file
                    try:
                        with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
                            content = f.read()
                        
                        for pattern in sensitive_patterns:
                            matches = re.findall(pattern, content, re.IGNORECASE)
                            if matches:
                                self.report["sensitive_data"].append({
                                    "file": str(file_path.relative_to(self.project_root)),
                                    "pattern": pattern,
                                    "matches": len(matches),
                                    "type": "sensitive_data"
                                })
                    except:
                        continue
    
    def analyze_security_configs(self):
        """Analisa configurações de segurança"""
        print("🔍 Analisando configurações de segurança...")
        
        config_files = [
            "security.conf",
            "auth.conf",
            "permissions.conf",
            "firewall.conf",
            "ssl.conf",
            "cors.conf",
            ".env",
            "config.json",
            "settings.json"
        ]
        
        for root, dirs, files in os.walk(self.project_root):
            for file in files:
                if file in config_files or any(ext in file for ext in ['.conf', '.config', '.env']):
                    file_path = Path(root) / file
                    try:
                        with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
                            content = f.read()
                        
                        # Verificar configurações de segurança
                        security_configs = [
                            "ssl_enabled",
                            "https_only",
                            "cors_enabled",
                            "csrf_protection",
                            "rate_limiting",
                            "session_timeout",
                            "max_login_attempts"
                        ]
                        
                        for config in security_configs:
                            if config in content:
                                self.report["security_configs"].append({
                                    "file": str(file_path.relative_to(self.project_root)),
                                    "config": config,
                                    "type": "security_setting"
                                })
                    except:
                        continue
    
    def calculate_security_metrics(self):
        """Calcula métricas de segurança"""
        print("🔍 Calculando métricas de segurança...")
        
        total_vulnerabilities = len(self.report["vulnerabilities"])
        high_severity = len([v for v in self.report["vulnerabilities"] if v["severity"] == "high"])
        medium_severity = len([v for v in self.report["vulnerabilities"] if v["severity"] == "medium"])
        
        total_auth_issues = len(self.report["authentication_issues"])
        total_permission_issues = len(self.report["permission_issues"])
        total_validation_issues = len(self.report["validation_issues"])
        total_sensitive_data = len(self.report["sensitive_data"])
        total_encryption_usage = len(self.report["encryption_usage"])
        total_security_configs = len(self.report["security_configs"])
        
        self.report["metrics"] = {
            "total_vulnerabilities": total_vulnerabilities,
            "high_severity_vulnerabilities": high_severity,
            "medium_severity_vulnerabilities": medium_severity,
            "authentication_issues": total_auth_issues,
            "permission_issues": total_permission_issues,
            "validation_issues": total_validation_issues,
            "sensitive_data_exposures": total_sensitive_data,
            "encryption_implementations": total_encryption_usage,
            "security_configurations": total_security_configs,
            "security_score": max(0, 100 - (high_severity * 10) - (medium_severity * 5) - (total_sensitive_data * 3))
        }
    
    def run_audit(self):
        """Executa auditoria completa de segurança"""
        print("🚀 Iniciando auditoria de segurança e validação...")
        
        self.analyze_security_patterns()
        self.analyze_authentication()
        self.analyze_permissions()
        self.analyze_validations()
        self.analyze_encryption_usage()
        self.analyze_sensitive_data()
        self.analyze_security_configs()
        self.calculate_security_metrics()
        
        # Salvar relatório
        report_path = self.project_root / "wiki" / "docs" / "audit_reports" / "security_audit_report.json"
        report_path.parent.mkdir(parents=True, exist_ok=True)
        
        with open(report_path, 'w', encoding='utf-8') as f:
            json.dump(self.report, f, indent=2, ensure_ascii=False)
        
        print(f"✅ Relatório salvo em: {report_path}")
        
        # Resumo
        print("\n📊 RESUMO DA AUDITORIA DE SEGURANÇA:")
        print(f"🚨 Vulnerabilidades encontradas: {self.report['metrics']['total_vulnerabilities']}")
        print(f"🔴 Severidade alta: {self.report['metrics']['high_severity_vulnerabilities']}")
        print(f"🟡 Severidade média: {self.report['metrics']['medium_severity_vulnerabilities']}")
        print(f"🔐 Problemas de autenticação: {self.report['metrics']['authentication_issues']}")
        print(f"🔒 Problemas de permissão: {self.report['metrics']['permission_issues']}")
        print(f"✅ Problemas de validação: {self.report['metrics']['validation_issues']}")
        print(f"⚠️ Dados sensíveis expostos: {self.report['metrics']['sensitive_data_exposures']}")
        print(f"🔐 Implementações de criptografia: {self.report['metrics']['encryption_implementations']}")
        print(f"⚙️ Configurações de segurança: {self.report['metrics']['security_configurations']}")
        print(f"📈 Score de segurança: {self.report['metrics']['security_score']}/100")
        
        return self.report

if __name__ == "__main__":
    import sys
    
    if len(sys.argv) > 1:
        project_root = sys.argv[1]
    else:
        project_root = "."
    
    auditor = SecurityAuditor(project_root)
    auditor.run_audit() 