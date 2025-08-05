#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
File System Auditor Agent
Responsável por auditar toda a estrutura de pastas e arquivos do projeto
"""

import os
import json
import hashlib
from datetime import datetime
from pathlib import Path
from typing import Dict, List, Set, Tuple
import argparse

class FileSystemAuditor:
    def __init__(self, project_root: str = "."):
        self.project_root = Path(project_root).resolve()
        self.audit_results = {
            "timestamp": datetime.now().isoformat(),
            "project_root": str(self.project_root),
            "total_files": 0,
            "total_directories": 0,
            "issues": [],
            "obsolete_items": [],
            "duplicate_files": [],
            "inconsistent_structures": [],
            "recommendations": []
        }
        
    def scan_project_structure(self) -> Dict:
        """Escaneia toda a estrutura do projeto"""
        print("🔍 Iniciando auditoria completa da estrutura do projeto...")
        
        # Estatísticas gerais
        for root, dirs, files in os.walk(self.project_root):
            self.audit_results["total_directories"] += len(dirs)
            self.audit_results["total_files"] += len(files)
        
        # Análises específicas
        self._analyze_obsolete_directories()
        self._analyze_duplicate_files()
        self._analyze_inconsistent_structures()
        self._analyze_empty_directories()
        self._analyze_file_extensions()
        self._analyze_naming_conventions()
        self._generate_recommendations()
        
        return self.audit_results
    
    def _analyze_obsolete_directories(self):
        """Identifica diretórios potencialmente obsoletos"""
        obsolete_patterns = [
            "backup", "old", "legacy", "deprecated", "temp", "tmp",
            "test_", "_test", "debug", "dev", "experimental"
        ]
        
        for root, dirs, files in os.walk(self.project_root):
            for dir_name in dirs:
                dir_path = Path(root) / dir_name
                relative_path = dir_path.relative_to(self.project_root)
                
                # Verifica padrões obsoletos
                for pattern in obsolete_patterns:
                    if pattern in dir_name.lower():
                        self.audit_results["obsolete_items"].append({
                            "type": "directory",
                            "path": str(relative_path),
                            "reason": f"Padrão obsoleto detectado: {pattern}",
                            "severity": "medium"
                        })
                        break
                
                # Verifica diretórios vazios ou com poucos arquivos
                try:
                    file_count = len(list(dir_path.rglob("*")))
                    if file_count <= 2:  # Poucos arquivos
                        self.audit_results["obsolete_items"].append({
                            "type": "directory",
                            "path": str(relative_path),
                            "reason": f"Diretório com apenas {file_count} arquivos",
                            "severity": "low"
                        })
                except PermissionError:
                    pass
    
    def _analyze_duplicate_files(self):
        """Identifica arquivos duplicados por conteúdo"""
        file_hashes = {}
        
        for root, dirs, files in os.walk(self.project_root):
            for file_name in files:
                file_path = Path(root) / file_name
                relative_path = file_path.relative_to(self.project_root)
                
                try:
                    # Calcula hash do arquivo
                    with open(file_path, 'rb') as f:
                        file_hash = hashlib.md5(f.read()).hexdigest()
                    
                    if file_hash in file_hashes:
                        self.audit_results["duplicate_files"].append({
                            "original": file_hashes[file_hash],
                            "duplicate": str(relative_path),
                            "hash": file_hash
                        })
                    else:
                        file_hashes[file_hash] = str(relative_path)
                        
                except (PermissionError, OSError):
                    pass
    
    def _analyze_inconsistent_structures(self):
        """Identifica estruturas inconsistentes"""
        # Verifica padrões de nomenclatura
        for root, dirs, files in os.walk(self.project_root):
            for dir_name in dirs:
                dir_path = Path(root) / dir_name
                relative_path = dir_path.relative_to(self.project_root)
                
                # Verifica mistura de estilos de nomenclatura
                has_underscore = '_' in dir_name
                has_hyphen = '-' in dir_name
                has_camelcase = any(c.isupper() for c in dir_name[1:])
                
                if (has_underscore and has_hyphen) or (has_underscore and has_camelcase):
                    self.audit_results["inconsistent_structures"].append({
                        "type": "naming_convention",
                        "path": str(relative_path),
                        "issue": "Mistura de estilos de nomenclatura",
                        "severity": "low"
                    })
    
    def _analyze_empty_directories(self):
        """Identifica diretórios vazios"""
        for root, dirs, files in os.walk(self.project_root):
            if not dirs and not files:
                relative_path = Path(root).relative_to(self.project_root)
                self.audit_results["issues"].append({
                    "type": "empty_directory",
                    "path": str(relative_path),
                    "severity": "medium",
                    "description": "Diretório vazio encontrado"
                })
    
    def _analyze_file_extensions(self):
        """Analisa extensões de arquivos"""
        extension_stats = {}
        
        for root, dirs, files in os.walk(self.project_root):
            for file_name in files:
                file_path = Path(root) / file_name
                extension = file_path.suffix.lower()
                
                if extension:
                    extension_stats[extension] = extension_stats.get(extension, 0) + 1
        
        # Identifica extensões incomuns
        common_extensions = {'.py', '.md', '.json', '.txt', '.lua', '.cpp', '.hpp', '.h', '.c', '.sh', '.bat', '.yml', '.yaml', '.toml', '.html', '.css', '.js', '.png', '.jpg', '.ico', '.rc', '.cmake', '.gradle', '.pro', '.proto'}
        
        for ext, count in extension_stats.items():
            if ext not in common_extensions and count > 1:
                self.audit_results["issues"].append({
                    "type": "unusual_extension",
                    "extension": ext,
                    "count": count,
                    "severity": "low",
                    "description": f"Extensão incomum encontrada {count} vezes"
                })
    
    def _analyze_naming_conventions(self):
        """Analisa convenções de nomenclatura"""
        for root, dirs, files in os.walk(self.project_root):
            for file_name in files:
                file_path = Path(root) / file_name
                relative_path = file_path.relative_to(self.project_root)
                
                # Verifica espaços em nomes de arquivos
                if ' ' in file_name:
                    self.audit_results["issues"].append({
                        "type": "naming_issue",
                        "path": str(relative_path),
                        "issue": "Espaços no nome do arquivo",
                        "severity": "medium"
                    })
                
                # Verifica caracteres especiais
                special_chars = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '+', '=', '{', '}', '[', ']', '|', '\\', ':', ';', '"', "'", '<', '>', ',', '?']
                for char in special_chars:
                    if char in file_name:
                        self.audit_results["issues"].append({
                            "type": "naming_issue",
                            "path": str(relative_path),
                            "issue": f"Caractere especial '{char}' no nome do arquivo",
                            "severity": "medium"
                        })
                        break
    
    def _generate_recommendations(self):
        """Gera recomendações baseadas na análise"""
        recommendations = []
        
        # Recomendações baseadas em problemas encontrados
        if self.audit_results["obsolete_items"]:
            recommendations.append({
                "category": "Limpeza",
                "action": "Remover diretórios e arquivos obsoletos",
                "priority": "high",
                "description": f"Encontrados {len(self.audit_results['obsolete_items'])} itens obsoletos"
            })
        
        if self.audit_results["duplicate_files"]:
            recommendations.append({
                "category": "Otimização",
                "action": "Consolidar arquivos duplicados",
                "priority": "medium",
                "description": f"Encontrados {len(self.audit_results['duplicate_files'])} arquivos duplicados"
            })
        
        if self.audit_results["inconsistent_structures"]:
            recommendations.append({
                "category": "Padronização",
                "action": "Padronizar convenções de nomenclatura",
                "priority": "medium",
                "description": f"Encontradas {len(self.audit_results['inconsistent_structures'])} inconsistências"
            })
        
        # Recomendações gerais
        recommendations.extend([
            {
                "category": "Documentação",
                "action": "Criar .gitignore abrangente",
                "priority": "medium",
                "description": "Para evitar commit de arquivos desnecessários"
            },
            {
                "category": "Organização",
                "action": "Criar estrutura de pastas padronizada",
                "priority": "high",
                "description": "Para melhor organização do projeto"
            },
            {
                "category": "Manutenção",
                "action": "Implementar limpeza automática",
                "priority": "low",
                "description": "Script para remoção periódica de arquivos temporários"
            }
        ])
        
        self.audit_results["recommendations"] = recommendations
    
    def save_report(self, output_file: str = "file_system_audit_report.json"):
        """Salva o relatório em arquivo JSON"""
        output_path = Path(output_file)
        
        with open(output_path, 'w', encoding='utf-8') as f:
            json.dump(self.audit_results, f, indent=2, ensure_ascii=False)
        
        print(f"📄 Relatório salvo em: {output_path}")
        return output_path
    
    def print_summary(self):
        """Imprime resumo da auditoria"""
        print("\n" + "="*60)
        print("📊 RESUMO DA AUDITORIA DE ESTRUTURA DE ARQUIVOS")
        print("="*60)
        
        print(f"📁 Total de diretórios: {self.audit_results['total_directories']}")
        print(f"📄 Total de arquivos: {self.audit_results['total_files']}")
        print(f"⚠️  Problemas encontrados: {len(self.audit_results['issues'])}")
        print(f"🗑️  Itens obsoletos: {len(self.audit_results['obsolete_items'])}")
        print(f"🔄 Arquivos duplicados: {len(self.audit_results['duplicate_files'])}")
        print(f"🔧 Inconsistências: {len(self.audit_results['inconsistent_structures'])}")
        print(f"💡 Recomendações: {len(self.audit_results['recommendations'])}")
        
        # Mostra problemas críticos
        critical_issues = [issue for issue in self.audit_results['issues'] if issue.get('severity') == 'high']
        if critical_issues:
            print(f"\n🚨 PROBLEMAS CRÍTICOS ({len(critical_issues)}):")
            for issue in critical_issues[:5]:  # Mostra apenas os 5 primeiros
                print(f"  • {issue['type']}: {issue.get('path', issue.get('description', 'N/A'))}")
        
        print("\n" + "="*60)

def main():
    parser = argparse.ArgumentParser(description="File System Auditor Agent")
    parser.add_argument("--project-root", default=".", help="Raiz do projeto para auditar")
    parser.add_argument("--output", default="file_system_audit_report.json", help="Arquivo de saída")
    parser.add_argument("--scan", action="store_true", help="Executar escaneamento completo")
    
    args = parser.parse_args()
    
    if args.scan:
        auditor = FileSystemAuditor(args.project_root)
        results = auditor.scan_project_structure()
        auditor.save_report(args.output)
        auditor.print_summary()
        
        return results
    
    print("🔍 File System Auditor Agent")
    print("Use --scan para executar a auditoria completa")

if __name__ == "__main__":
    main() 