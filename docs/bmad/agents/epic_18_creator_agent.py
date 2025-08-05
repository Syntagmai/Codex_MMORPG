#!/usr/bin/env python3
"""
Epic 18 Creator Agent - Epic 17 Task 17.8
Cria Epic 18 com plano detalhado de correção dos problemas identificados
"""

import os
import json
import re
from datetime import datetime
from pathlib import Path

class Epic18Creator:
    def __init__(self, project_root):
        self.project_root = Path(project_root)
        self.audit_reports_dir = self.project_root / "wiki" / "docs" / "audit_reports"
        self.epic_18_data = {
            "epic_number": 18,
            "name": "Correção e Otimização do Sistema",
            "status": "0%",
            "priority": "Crítica",
            "objective": "Corrigir todos os problemas identificados na Epic 17 e otimizar o sistema",
            "created_date": datetime.now().isoformat(),
            "tasks": [],
            "critical_issues": [],
            "optimization_opportunities": [],
            "security_fixes": [],
            "performance_improvements": [],
            "documentation_updates": [],
            "integration_fixes": []
        }
    
    def load_audit_reports(self):
        """Carrega todos os relatórios de auditoria da Epic 17"""
        print("📊 Carregando relatórios de auditoria da Epic 17...")
        
        audit_files = [
            "file_structure_audit_report.json",
            "python_audit_report.json", 
            "config_audit_report.json",
            "documentation_audit_report.json",
            "integration_audit_report.json",
            "performance_audit_report.json",
            "security_audit_report.json"
        ]
        
        reports = {}
        for audit_file in audit_files:
            file_path = self.audit_reports_dir / audit_file
            if file_path.exists():
                try:
                    with open(file_path, 'r', encoding='utf-8') as f:
                        reports[audit_file] = json.load(f)
                    print(f"✅ Carregado: {audit_file}")
                except Exception as e:
                    print(f"❌ Erro ao carregar {audit_file}: {e}")
            else:
                print(f"⚠️ Arquivo não encontrado: {audit_file}")
        
        return reports
    
    def analyze_critical_issues(self, reports):
        """Analisa problemas críticos identificados"""
        print("🔍 Analisando problemas críticos...")
        
        critical_issues = []
        
        # Problemas de segurança (alta prioridade)
        if "security_audit_report.json" in reports:
            security_data = reports["security_audit_report.json"]
            # Extrair problemas de segurança baseado na estrutura real
            auth_issues = security_data.get("authentication_issues", [])
            permission_issues = security_data.get("permission_issues", [])
            validation_issues = security_data.get("validation_issues", [])
            
            # Adicionar problemas críticos de autenticação
            for issue in auth_issues[:5]:
                critical_issues.append({
                    "type": "security_auth",
                    "description": f"Problema de autenticação: {issue.get('type', 'N/A')}",
                    "file": issue.get("file", "N/A"),
                    "priority": "Alta",
                    "epic_18_task": "18.1"
                })
            
            # Adicionar problemas de permissão
            for issue in permission_issues[:5]:
                critical_issues.append({
                    "type": "security_permission",
                    "description": f"Problema de permissão: {issue.get('type', 'N/A')}",
                    "file": issue.get("file", "N/A"),
                    "priority": "Alta",
                    "epic_18_task": "18.1"
                })
        
        # Erros de sintaxe Python (alta prioridade)
        if "python_audit_report.json" in reports:
            python_data = reports["python_audit_report.json"]
            syntax_errors = python_data.get("syntax_errors", [])
            for error in syntax_errors[:10]:  # Top 10 mais críticos
                critical_issues.append({
                    "type": "python_syntax",
                    "description": f"Erro de sintaxe Python: {error.get('error', 'N/A')}",
                    "file": error.get("file", "N/A"),
                    "line": error.get("line", "N/A"),
                    "priority": "Alta",
                    "epic_18_task": "18.2"
                })
        
        # Arquivos grandes que impactam performance
        if "performance_audit_report.json" in reports:
            perf_data = reports["performance_audit_report.json"]
            large_files = perf_data.get("large_files", [])
            for file_info in large_files[:5]:  # Top 5 maiores
                critical_issues.append({
                    "type": "performance_large_file",
                    "description": f"Arquivo muito grande: {file_info.get('size_mb', 0)} MB",
                    "file": file_info.get("path", "N/A"),
                    "priority": "Média",
                    "epic_18_task": "18.3"
                })
        
        # Dependências circulares críticas
        if "integration_audit_report.json" in reports:
            integration_data = reports["integration_audit_report.json"]
            circular_deps = integration_data.get("circular_dependencies", [])
            for dep in circular_deps[:5]:  # Top 5 mais críticas
                critical_issues.append({
                    "type": "integration_circular",
                    "description": f"Dependência circular: {dep.get('description', 'N/A')}",
                    "files": dep.get("files", []),
                    "priority": "Alta",
                    "epic_18_task": "18.4"
                })
        
        self.epic_18_data["critical_issues"] = critical_issues
        return critical_issues
    
    def create_optimization_tasks(self, reports):
        """Cria tasks de otimização baseadas nos relatórios"""
        print("🔧 Criando tasks de otimização...")
        
        tasks = []
        task_counter = 1
        
        # Task 18.1: Correção de Vulnerabilidades de Segurança
        tasks.append({
            "task_number": f"18.{task_counter}",
            "name": "Correção de Vulnerabilidades de Segurança",
            "description": "Corrigir vulnerabilidades de alta e média severidade identificadas",
            "priority": "Crítica",
            "estimated_hours": 16,
            "dependencies": [],
            "subtasks": [
                "Corrigir 5 vulnerabilidades de alta severidade",
                "Corrigir 50 vulnerabilidades de média severidade",
                "Implementar validações de entrada robustas",
                "Corrigir problemas de autenticação",
                "Corrigir problemas de permissão",
                "Proteger dados sensíveis expostos"
            ]
        })
        task_counter += 1
        
        # Task 18.2: Correção de Erros de Sintaxe Python
        tasks.append({
            "task_number": f"18.{task_counter}",
            "name": "Correção de Erros de Sintaxe Python",
            "description": "Corrigir erros de sintaxe e imports obsoletos em scripts Python",
            "priority": "Alta",
            "estimated_hours": 12,
            "dependencies": [],
            "subtasks": [
                "Corrigir 389 erros de sintaxe Python",
                "Remover 418 imports obsoletos unicode_aliases",
                "Instalar 753 dependências faltantes",
                "Validar sintaxe de todos os scripts",
                "Testar execução dos scripts corrigidos"
            ]
        })
        task_counter += 1
        
        # Task 18.3: Otimização de Performance
        tasks.append({
            "task_number": f"18.{task_counter}",
            "name": "Otimização de Performance e Recursos",
            "description": "Otimizar arquivos grandes, scripts lentos e gargalos identificados",
            "priority": "Alta",
            "estimated_hours": 20,
            "dependencies": ["18.2"],
            "subtasks": [
                "Otimizar 20 arquivos grandes (>1MB)",
                "Melhorar 15 scripts lentos identificados",
                "Corrigir 20 gargalos potenciais",
                "Implementar 15 oportunidades de otimização",
                "Reduzir uso de memória e CPU",
                "Otimizar operações de I/O"
            ]
        })
        task_counter += 1
        
        # Task 18.4: Correção de Integrações e Dependências
        tasks.append({
            "task_number": f"18.{task_counter}",
            "name": "Correção de Integrações e Dependências",
            "description": "Corrigir dependências circulares, interfaces quebradas e integrações críticas",
            "priority": "Alta",
            "estimated_hours": 18,
            "dependencies": ["18.2"],
            "subtasks": [
                "Resolver 661 dependências circulares",
                "Corrigir 223 interfaces quebradas",
                "Otimizar 424 integrações críticas",
                "Melhorar 795 fluxos de dados",
                "Corrigir 88 endpoints de API",
                "Validar todas as integrações"
            ]
        })
        task_counter += 1
        
        # Task 18.5: Limpeza de Estrutura de Arquivos
        tasks.append({
            "task_number": f"18.{task_counter}",
            "name": "Limpeza de Estrutura de Arquivos",
            "description": "Remover itens obsoletos, diretórios vazios e problemas de nomenclatura",
            "priority": "Média",
            "estimated_hours": 8,
            "dependencies": [],
            "subtasks": [
                "Remover 104 itens obsoletos",
                "Limpar 137 diretórios vazios",
                "Corrigir 4 problemas de nomenclatura",
                "Organizar estrutura de pastas",
                "Validar organização final"
            ]
        })
        task_counter += 1
        
        # Task 18.6: Correção de Configurações
        tasks.append({
            "task_number": f"18.{task_counter}",
            "name": "Correção de Configurações e Regras",
            "description": "Corrigir configurações obsoletas e parâmetros inconsistentes",
            "priority": "Média",
            "estimated_hours": 6,
            "dependencies": [],
            "subtasks": [
                "Remover 131 configurações obsoletas",
                "Corrigir 4 parâmetros inconsistentes",
                "Resolver 109 problemas gerais de configuração",
                "Validar todas as configurações",
                "Testar funcionamento do sistema"
            ]
        })
        task_counter += 1
        
        # Task 18.7: Correção de Documentação
        tasks.append({
            "task_number": f"18.{task_counter}",
            "name": "Correção de Documentação e Wikis",
            "description": "Corrigir links quebrados, documentos incompletos e problemas de qualidade",
            "priority": "Média",
            "estimated_hours": 10,
            "dependencies": [],
            "subtasks": [
                "Corrigir 7,208 links quebrados",
                "Completar 239 documentos incompletos",
                "Criar 2 documentações críticas faltantes (CHANGELOG.md, LICENSE)",
                "Corrigir 21 problemas de qualidade",
                "Validar toda a documentação"
            ]
        })
        task_counter += 1
        
        # Task 18.8: Atualização do README.md Principal
        tasks.append({
            "task_number": f"18.{task_counter}",
            "name": "Atualização do README.md Principal",
            "description": "Criar versão estável e transparente do README.md principal",
            "priority": "Alta",
            "estimated_hours": 4,
            "dependencies": ["18.7"],
            "subtasks": [
                "Criar estrutura clara e organizada",
                "Documentar todas as funcionalidades",
                "Incluir guias de instalação e uso",
                "Adicionar exemplos práticos",
                "Validar clareza e transparência"
            ]
        })
        task_counter += 1
        
        # Task 18.9: Testes e Validação
        tasks.append({
            "task_number": f"18.{task_counter}",
            "name": "Testes e Validação Completa",
            "description": "Realizar testes abrangentes para validar todas as correções",
            "priority": "Alta",
            "estimated_hours": 12,
            "dependencies": ["18.1", "18.2", "18.3", "18.4", "18.5", "18.6", "18.7", "18.8"],
            "subtasks": [
                "Testes de segurança",
                "Testes de performance",
                "Testes de integração",
                "Testes de documentação",
                "Validação final do sistema"
            ]
        })
        task_counter += 1
        
        # Task 18.10: Relatório Final de Correção
        tasks.append({
            "task_number": f"18.{task_counter}",
            "name": "Relatório Final de Correção e Otimização",
            "description": "Gerar relatório final consolidado com todas as correções realizadas",
            "priority": "Média",
            "estimated_hours": 3,
            "dependencies": ["18.9"],
            "subtasks": [
                "Consolidar resultados de todas as correções",
                "Documentar melhorias implementadas",
                "Criar métricas de antes e depois",
                "Gerar relatório executivo",
                "Arquivar Epic 18 como concluída"
            ]
        })
        
        self.epic_18_data["tasks"] = tasks
        return tasks
    
    def calculate_metrics(self):
        """Calcula métricas da Epic 18"""
        print("📊 Calculando métricas da Epic 18...")
        
        total_tasks = len(self.epic_18_data["tasks"])
        total_hours = sum(task.get("estimated_hours", 0) for task in self.epic_18_data["tasks"])
        critical_issues = len([issue for issue in self.epic_18_data["critical_issues"] if issue.get("priority") == "Crítica"])
        
        metrics = {
            "total_tasks": total_tasks,
            "total_estimated_hours": total_hours,
            "critical_issues_to_fix": critical_issues,
            "priority_distribution": {
                "Crítica": len([task for task in self.epic_18_data["tasks"] if task.get("priority") == "Crítica"]),
                "Alta": len([task for task in self.epic_18_data["tasks"] if task.get("priority") == "Alta"]),
                "Média": len([task for task in self.epic_18_data["tasks"] if task.get("priority") == "Média"]),
                "Baixa": len([task for task in self.epic_18_data["tasks"] if task.get("priority") == "Baixa"])
            }
        }
        
        self.epic_18_data["metrics"] = metrics
        return metrics
    
    def create_epic_18_markdown(self):
        """Cria o arquivo markdown da Epic 18"""
        print("📝 Criando arquivo markdown da Epic 18...")
        
        epic_18_content = f"""# 🛠️ Epic 18: Correção e Otimização do Sistema

## 📋 **INFORMAÇÕES GERAIS**

- **Status**: 0%
- **Prioridade**: Crítica
- **Data de Criação**: {self.epic_18_data['created_date']}
- **Tempo Estimado**: {self.epic_18_data['metrics']['total_estimated_hours']} horas
- **Total de Tasks**: {self.epic_18_data['metrics']['total_tasks']}

## 🎯 **OBJETIVO**

{self.epic_18_data['objective']}

## 📊 **MÉTRICAS**

- **Tasks Críticas**: {self.epic_18_data['metrics']['priority_distribution']['Crítica']}
- **Tasks Altas**: {self.epic_18_data['metrics']['priority_distribution']['Alta']}
- **Tasks Médias**: {self.epic_18_data['metrics']['priority_distribution']['Média']}
- **Problemas Críticos a Corrigir**: {self.epic_18_data['metrics']['critical_issues_to_fix']}

## 🚨 **PROBLEMAS CRÍTICOS IDENTIFICADOS**

"""
        
        for issue in self.epic_18_data["critical_issues"][:10]:  # Top 10
            epic_18_content += f"- **{issue['type'].upper()}**: {issue['description']} (Prioridade: {issue['priority']})\n"
        
        epic_18_content += "\n## 📋 **TASKS DA EPIC 18**\n\n"
        
        for task in self.epic_18_data["tasks"]:
            epic_18_content += f"""### **{task['task_number']} {task['name']}**
- **Status**: ⏳ PENDENTE
- **Progresso**: 0%
- **Prioridade**: {task['priority']}
- **Tempo Estimado**: {task['estimated_hours']} horas
- **Dependências**: {', '.join(task['dependencies']) if task['dependencies'] else 'Nenhuma'}

**Descrição**: {task['description']}

**Subtasks:**
"""
            for subtask in task['subtasks']:
                epic_18_content += f"- [ ] {subtask}\n"
            
            epic_18_content += "\n"
        
        epic_18_content += """## 🎯 **CRITÉRIOS DE CONCLUSÃO**

- [ ] Todas as vulnerabilidades de segurança corrigidas
- [ ] Todos os erros de sintaxe Python resolvidos
- [ ] Performance otimizada conforme métricas estabelecidas
- [ ] Integrações funcionando corretamente
- [ ] Documentação completa e atualizada
- [ ] README.md principal atualizado e transparente
- [ ] Testes de validação passando
- [ ] Relatório final consolidado

## 📈 **MÉTRICAS DE SUCESSO**

- **Score de Segurança**: > 80/100
- **Erros de Sintaxe**: 0
- **Performance**: Melhoria de pelo menos 30%
- **Documentação**: 100% dos links funcionando
- **Integrações**: 100% funcionando corretamente

---

> [!info] **EPIC 18 CRIADA**
> Esta Epic foi criada automaticamente pelo Epic 18 Creator Agent baseado nos resultados da Epic 17.
> Todas as tasks foram planejadas para corrigir os problemas identificados nas auditorias.
"""
        
        # Salvar arquivo da Epic 18
        epic_18_file = self.project_root / "wiki" / "dashboard" / "epic_18_correction_plan.md"
        with open(epic_18_file, 'w', encoding='utf-8') as f:
            f.write(epic_18_content)
        
        print(f"✅ Epic 18 criada: {epic_18_file}")
        return epic_18_file
    
    def update_task_master(self):
        """Atualiza o task_master.md com a Epic 18"""
        print("📋 Atualizando task_master.md com Epic 18...")
        
        task_master_file = self.project_root / "wiki" / "dashboard" / "task_master.md"
        
        if not task_master_file.exists():
            print("❌ task_master.md não encontrado")
            return False
        
        try:
            with open(task_master_file, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # Adicionar Epic 18 após a Epic 17
            epic_17_section = "## 🎯 **EPIC 17: VERIFICAÇÃO GERAL COMPLETA DO SISTEMA**"
            epic_18_section = f"""

## 🛠️ **EPIC 18: CORREÇÃO E OTIMIZAÇÃO DO SISTEMA**

### **Status**: 0%
### **Prioridade**: Crítica
### **Objetivo**: {self.epic_18_data['objective']}

### **Tasks da Epic 18:**

"""
            
            for task in self.epic_18_data["tasks"]:
                epic_18_section += f"""- [ ] **{task['task_number']}** {task['name']} (0% → 0%) ⏳ **PENDENTE**
  - **Descrição**: {task['description']}
  - **Prioridade**: {task['priority']}
  - **Tempo Estimado**: {task['estimated_hours']} horas
  - **Dependências**: {', '.join(task['dependencies']) if task['dependencies'] else 'Nenhuma'}

"""
            
            # Inserir Epic 18 após Epic 17
            if epic_17_section in content:
                new_content = content.replace(epic_17_section, epic_17_section + epic_18_section)
                
                with open(task_master_file, 'w', encoding='utf-8') as f:
                    f.write(new_content)
                
                print("✅ task_master.md atualizado com Epic 18")
                return True
            else:
                print("❌ Seção Epic 17 não encontrada no task_master.md")
                return False
                
        except Exception as e:
            print(f"❌ Erro ao atualizar task_master.md: {e}")
            return False
    
    def create_json_report(self):
        """Cria relatório JSON da Epic 18"""
        print("📊 Criando relatório JSON da Epic 18...")
        
        report_file = self.audit_reports_dir / "epic_18_creation_report.json"
        
        with open(report_file, 'w', encoding='utf-8') as f:
            json.dump(self.epic_18_data, f, indent=2, ensure_ascii=False)
        
        print(f"✅ Relatório JSON criado: {report_file}")
        return report_file
    
    def run_creation(self):
        """Executa a criação completa da Epic 18"""
        print("🚀 Iniciando criação da Epic 18...")
        
        # Carregar relatórios de auditoria
        reports = self.load_audit_reports()
        
        # Analisar problemas críticos
        critical_issues = self.analyze_critical_issues(reports)
        
        # Criar tasks de otimização
        tasks = self.create_optimization_tasks(reports)
        
        # Calcular métricas
        metrics = self.calculate_metrics()
        
        # Criar arquivo markdown
        epic_18_file = self.create_epic_18_markdown()
        
        # Atualizar task_master.md
        task_master_updated = self.update_task_master()
        
        # Criar relatório JSON
        json_report = self.create_json_report()
        
        # Resumo final
        print("\n" + "="*60)
        print("📊 RESUMO DA CRIAÇÃO DA EPIC 18")
        print("="*60)
        print(f"📋 Total de tasks criadas: {len(tasks)}")
        print(f"⏰ Tempo total estimado: {metrics['total_estimated_hours']} horas")
        print(f"🚨 Problemas críticos identificados: {len(critical_issues)}")
        print(f"📝 Arquivo Epic 18 criado: {epic_18_file}")
        print(f"📋 Task Master atualizado: {'✅' if task_master_updated else '❌'}")
        print(f"📊 Relatório JSON criado: {json_report}")
        print("="*60)
        
        return {
            "epic_18_file": str(epic_18_file),
            "task_master_updated": task_master_updated,
            "json_report": str(json_report),
            "total_tasks": len(tasks),
            "total_hours": metrics['total_estimated_hours'],
            "critical_issues": len(critical_issues)
        }

if __name__ == "__main__":
    import sys
    
    if len(sys.argv) > 1:
        project_root = sys.argv[1]
    else:
        project_root = "."
    
    creator = Epic18Creator(project_root)
    result = creator.run_creation() 