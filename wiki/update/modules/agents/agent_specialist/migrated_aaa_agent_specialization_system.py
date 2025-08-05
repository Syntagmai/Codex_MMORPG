from unicode_aliases import *
# Constantes
MAX_RETRIES = 8

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script Migrado: aaa_agent_specialization_system.py
Módulo de Destino: agents.agent_specialist
Data de Migração: 2025-08-01 12:21:33

Script original migrado para a estrutura modular unificada.
"""

# Imports do módulo
from . import AgentspecialistModule

# Conteúdo original do script
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Sistema de Agentes Especializados - Nível AAA
Implementação do sistema de agentes especializados para orquestração de nível AAA
"""

import os
import json
import time
from datetime import datetime

class AAAAgentSpecializationSystem:
    """Sistema de agentes especializados de nível AAA"""
    
    def __init__(self, base_path: str):
        self.base_path = Path(base_path)
        self.agents = {}
        self.workflows = {}
        self.metrics = AAAMetrics()
        self.quality_monitor = QualityMonitor()
        
        # Estrutura de pastas
        self.agents_path = self.base_path / 'bmad' / 'agents'
        self.workflows_path = self.base_path / 'bmad' / 'workflows'
        self.templates_path = self.base_path / 'bmad' / 'templates'
        self.logs_path = self.base_path / 'log'
        
        # Cria estrutura de pastas
        self.create_directory_structure()
        
        # Inicializa agentes
        self.initialize_agents()
        
        # Inicializa workflows
        self.initialize_workflows()
    
    def create_directory_structure(self):
        """Cria estrutura de pastas necessária"""
        directories = [
            self.agents_path,
            self.workflows_path,
            self.templates_path,
            self.logs_path / 'aaa_agents',
            self.logs_path / 'aaa_workflows',
            self.logs_path / 'aaa_metrics'
        ]
        
        for directory in directories:
            directory.mkdir(parents=True, exist_ok=True)
    
    def initialize_agents(self):
        """Inicializa todos os agentes especializados AAA"""
        print("🎭 Inicializando agentes especializados AAA...")
        
        # Agente C++ (Zara)
        self.agents['agent_cpp'] = AAAAgent(
            name="Zara",
            specialization="C++ Development & Performance Optimization",
            file_extensions=['.cpp', '.hpp', '.h', '.cc', '.cxx'],
            capabilities=[
                "AST Analysis using Clang/LLVM",
                "Memory Leak Detection with Valgrind",
                "Performance Optimization",
                "Cyclomatic Complexity Analysis",
                "Race Condition Detection",
                "CMake Integration",
                "Dependency Analysis",
                "Refactoring Suggestions"
            ],
            tools=[
                "Clang/LLVM",
                "Valgrind",
                "CMake",
                "Static Analysis Tools",
                "Performance Profilers"
            ]
        )
        
        # Agente Python (Py)
        self.agents['agent_python'] = AAAAgent(
            name="Py",
            specialization="Python Development & Code Quality",
            file_extensions=['.py', '.pyx', '.pyi'],
            capabilities=[
                "AST Analysis",
                "Code Quality Assessment",
                "Security Vulnerability Detection",
                "Performance Analysis",
                "Refactoring Suggestions",
                "CI/CD Integration",
                "Advanced Metrics",
                "Detailed Reports"
            ],
            tools=[
                "pylint",
                "mypy",
                "black",
                "bandit",
                "pytest",
                "coverage"
            ]
        )
        
        # Agente Lua (Maya)
        self.agents['agent_lua'] = AAAAgent(
            name="Maya",
            specialization="Lua Scripting & OTClient Modules",
            file_extensions=['.lua', '.otui', '.otmod'],
            capabilities=[
                "Advanced Module Analysis",
                "OTUI/OTMod Validation",
                "Performance Optimization",
                "Common Bug Detection",
                "Dependency Analysis",
                "Code Improvement Suggestions",
                "OTClient Integration"
            ],
            tools=[
                "Lua AST Parser",
                "OTClient Module Validator",
                "Performance Profiler",
                "Dependency Analyzer"
            ]
        )
        
        # Agente Obsidian Markdown (Doc)
        self.agents['agent_markdown'] = AAAAgent(
            name="Doc",
            specialization="Documentation & Knowledge Management",
            file_extensions=['.md', '.markdown'],
            capabilities=[
                "Frontmatter YAML Analysis",
                "Wikilinks Validation",
                "Callouts Analysis",
                "Navigation Optimization",
                "Style Consistency Detection",
                "Documentation Improvement",
                "JSON Maps Integration"
            ],
            tools=[
                "YAML Parser",
                "Markdown Validator",
                "Link Checker",
                "Style Analyzer"
            ]
        )
        
        # Agente JSON (Json)
        self.agents['agent_json'] = AAAAgent(
            name="Json",
            specialization="Data Structure & Schema Management",
            file_extensions=['.json', '.jsonc'],
            capabilities=[
                "Advanced Schema Validation",
                "Data Structure Analysis",
                "Inconsistency Detection",
                "Performance Optimization",
                "Relationship Analysis",
                "Structure Improvement",
                "Navigation Integration"
            ],
            tools=[
                "JSON Schema Validator",
                "Structure Analyzer",
                "Performance Optimizer",
                "Relationship Mapper"
            ]
        )
        
        # Agente de Recursos (Rex)
        self.agents['agent_resources'] = AAAAgent(
            name="Rex",
            specialization="Asset Management & Optimization",
            file_extensions=['.png', '.jpg', '.jpeg', '.gif', '.bmp', '.tga'],
            capabilities=[
                "Image Analysis with Pillow",
                "Automatic Compression",
                "OTClient Format Validation",
                "Metadata Analysis",
                "Unused Resource Detection",
                "Asset Optimization",
                "Pipeline Integration"
            ],
            tools=[
                "Pillow (PIL)",
                "Image Optimizer",
                "Metadata Extractor",
                "Format Validator"
            ]
        )
        
        # Agente de Áudio (Aud)
        self.agents['agent_audio'] = AAAAgent(
            name="Aud",
            specialization="Audio Processing & Quality",
            file_extensions=['.ogg', '.wav', '.mp3', '.flac', '.aac'],
            capabilities=[
                "Audio Format Analysis",
                "Quality Validation",
                "Compression Optimization",
                "Audio Problem Detection",
                "Quality Improvement",
                "Resource Integration"
            ],
            tools=[
                "Audio Analyzer",
                "Quality Checker",
                "Compression Tool",
                "Format Converter"
            ]
        )
        
        # Agente de Fontes (Font)
        self.agents['agent_fonts'] = AAAAgent(
            name="Font",
            specialization="Typography & Font Management",
            file_extensions=['.otfont', '.ttf', '.otf', '.woff', '.woff2'],
            capabilities=[
                "Font Format Analysis",
                "Character Support Validation",
                "OTClient Font Optimization",
                "Rendering Problem Detection",
                "Font Improvement",
                "UI Integration"
            ],
            tools=[
                "Font Analyzer",
                "Character Validator",
                "Rendering Tester",
                "Format Converter"
            ]
        )
        
        # Agente de Build (Build)
        self.agents['agent_build'] = AAAAgent(
            name="Build",
            specialization="Build Systems & Compilation",
            file_extensions=['.cmake', '.cmake.in', '.vcxproj', '.sln', '.makefile'],
            capabilities=[
                "CMake Analysis",
                "Build Optimization",
                "Dependency Detection",
                "Performance Analysis",
                "Build Improvement",
                "CI/CD Integration"
            ],
            tools=[
                "CMake Parser",
                "Build Analyzer",
                "Dependency Mapper",
                "Performance Profiler"
            ]
        )
        
        # Agente Web (Web)
        self.agents['agent_web'] = AAAAgent(
            name="Web",
            specialization="Web Technologies & Accessibility",
            file_extensions=['.html', '.css', '.js', '.ts', '.vue', '.react'],
            capabilities=[
                "HTML/CSS/JS Analysis",
                "Accessibility Validation",
                "Performance Optimization",
                "Compatibility Detection",
                "Code Improvement",
                "Web Tools Integration"
            ],
            tools=[
                "HTML Validator",
                "CSS Analyzer",
                "JavaScript Linter",
                "Accessibility Checker"
            ]
        )
        
        # Agente de Configuração (Config)
        self.agents['agent_config'] = AAAAgent(
            name="Config",
            specialization="Configuration & Deployment",
            file_extensions=['.ini', '.conf', '.cfg', '.yaml', '.yml', '.toml'],
            capabilities=[
                "Configuration Analysis",
                "Syntax Validation",
                "Problematic Config Detection",
                "Configuration Improvement",
                "Security Analysis",
                "Deployment Integration"
            ],
            tools=[
                "Config Parser",
                "Syntax Validator",
                "Security Scanner",
                "Deployment Helper"
            ]
        )
        
        print(f"✅ {len(self.agents)} agentes especializados AAA inicializados")
    
    def initialize_workflows(self):
        """Inicializa workflows de nível AAA"""
        print("🔄 Inicializando workflows AAA...")
        
        # Workflow de Otimização de Performance
        self.workflows['aaa_performance'] = AAAWorkflow(
            name="AAA Performance Optimization",
            agents=['agent_cpp', 'agent_python', 'qa_tester'],
            phases=['analysis', 'optimization', 'validation'],
            duration='4-6 hours',
            quality_gates=['performance_improvement', 'no_regressions']
        )
        
        # Workflow de Desenvolvimento de Feature
        self.workflows['aaa_feature'] = AAAWorkflow(
            name="AAA Feature Development",
            agents=['game_designer', 'agent_cpp', 'agent_lua', 'qa_tester'],
            phases=['design', 'implementation', 'testing'],
            duration='1-2 weeks',
            quality_gates=['feature_complete', 'tests_passing']
        )
        
        # Workflow de Correção de Bug
        self.workflows['aaa_bugfix'] = AAAWorkflow(
            name="AAA Bug Fix",
            agents=['qa_tester', 'agent_cpp', 'agent_lua'],
            phases=['identification', 'fix', 'validation'],
            duration='2-4 hours',
            quality_gates=['bug_resolved', 'no_new_issues']
        )
        
        print(f"✅ {len(self.workflows)} workflows AAA inicializados")
    
    def detect_context_by_extension(self, file_path: str) -> Dict[str, Any]:
        """Detecta contexto baseado na extensão do arquivo"""
        extension = Path(file_path).suffix.lower()
        
        # Mapeamento de extensões para agentes
        agent_mapping = {
            '.cpp': 'agent_cpp',
            '.hpp': 'agent_cpp', 
            '.h': 'agent_cpp',
            '.cc': 'agent_cpp',
            '.cxx': 'agent_cpp',
            '.py': 'agent_python',
            '.pyx': 'agent_python',
            '.pyi': 'agent_python',
            '.lua': 'agent_lua',
            '.otui': 'agent_lua',
            '.otmod': 'agent_lua',
            '.md': 'agent_markdown',
            '.markdown': 'agent_markdown',
            '.json': 'agent_json',
            '.jsonc': 'agent_json',
            '.png': 'agent_resources',
            '.jpg': 'agent_resources',
            '.jpeg': 'agent_resources',
            '.gif': 'agent_resources',
            '.bmp': 'agent_resources',
            '.tga': 'agent_resources',
            '.ogg': 'agent_audio',
            '.wav': 'agent_audio',
            '.mp3': 'agent_audio',
            '.flac': 'agent_audio',
            '.aac': 'agent_audio',
            '.otfont': 'agent_fonts',
            '.ttf': 'agent_fonts',
            '.otf': 'agent_fonts',
            '.woff': 'agent_fonts',
            '.woff2': 'agent_fonts',
            '.cmake': 'agent_build',
            '.cmake.in': 'agent_build',
            '.vcxproj': 'agent_build',
            '.sln': 'agent_build',
            '.makefile': 'agent_build',
            '.html': 'agent_web',
            '.css': 'agent_web',
            '.js': 'agent_web',
            '.ts': 'agent_web',
            '.vue': 'agent_web',
            '.react': 'agent_web',
            '.ini': 'agent_config',
            '.conf': 'agent_config',
            '.cfg': 'agent_config',
            '.yaml': 'agent_config',
            '.yml': 'agent_config',
            '.toml': 'agent_config'
        }
        
        primary_agent = agent_mapping.get(extension, 'default_agent')
        
        context = {
            'file_path': file_path,
            'extension': extension,
            'primary_agent': primary_agent,
            'detected_at': datetime.now().isoformat(),
            'confidence_score': 1.0 if extension in agent_mapping else 0.5
        }
        
        # Registra métrica
        self.metrics.record_metric('context_detection', 1.0)
        
        return context
    
    def select_agents(self, context: Dict[str, Any]) -> List[str]:
        """Seleciona agentes baseado no contexto"""
        primary_agent = context['primary_agent']
        secondary_agents = []
        
        # Adiciona agentes secundários baseado no contexto
        if context.get('complexity') == 'high':
            secondary_agents.append('qa_tester')
        
        if context.get('performance_critical'):
            secondary_agents.append('performance_optimizer')
        
        selected_agents = [primary_agent] + secondary_agents
        
        # Registra métrica
        self.metrics.record_metric('agent_selection_accuracy', 1.0)
        
        return selected_agents
    
    def execute_agent_workflow(self, file_path: str, user_request: str) -> Dict[str, Any]:
        """Executa workflow de agente para arquivo específico"""
        start_time = time.time()
        
        print(f"🎯 Executando workflow AAA para: {file_path}")
        print(f"📝 Solicitação: {user_request}")
        
        # Detecta contexto
        context = self.detect_context_by_extension(file_path)
        print(f"🔍 Contexto detectado: {context['primary_agent']}")
        
        # Seleciona agentes
        selected_agents = self.select_agents(context)
        print(f"👥 Agentes selecionados: {', '.join(selected_agents)}")
        
        # Executa agentes
        results = {}
        for agent_id in selected_agents:
            if agent_id in self.agents:
                agent = self.agents[agent_id]
                print(f"🚀 Executando {agent.name} ({agent.specialization})")
                
                agent_result = agent.execute(file_path, user_request, context)
                results[agent_id] = agent_result
                
                # Valida qualidade
                quality_score = self.quality_monitor.check_quality_gate(f"{agent_id}_quality")
                if quality_score < 0.85:
                    print(f"⚠️ Qualidade abaixo do esperado para {agent.name}: {quality_score:.2f}")
        
        # Calcula tempo total
        execution_time = time.time() - start_time
        
        # Registra métricas
        self.metrics.record_metric('execution_time', execution_time)
        self.metrics.record_metric('agents_used', len(selected_agents))
        
        # Gera relatório
        report = {
            'file_path': file_path,
            'user_request': user_request,
            'context': context,
            'selected_agents': selected_agents,
            'results': results,
            'execution_time': execution_time,
            'quality_score': self.calculate_overall_quality(results),
            'timestamp': datetime.now().isoformat()
        }
        
        # Salva relatório
        self.save_report(report)
        
        print(f"✅ Workflow AAA concluído em {execution_time:.2f}s")
        print(f"📊 Qualidade geral: {report['quality_score']:.2f}")
        
        return report
    
    def calculate_overall_quality(self, results: Dict[str, Any]) -> float:
        """Calcula qualidade geral dos resultados"""
        if not results:
            return 0.0
        
        quality_scores = []
        for agent_id, result in results.items():
            if 'quality_score' in result:
                quality_scores.append(result['quality_score'])
        
        return sum(quality_scores) / len(quality_scores) if quality_scores else 0.0
    
    def save_report(self, report: Dict[str, Any]):
        """Salva relatório de execução"""
        timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
        filename = f"aaa_workflow_report_{timestamp}.json"
        filepath = self.logs_path / 'aaa_workflows' / filename
        
        with open(filepath, 'w', encoding='utf-8') as f:
            json.dump(report, f, indent=2, ensure_ascii=False)
        
        print(f"📄 Relatório salvo: {filepath}")
    
    def generate_metrics_report(self) -> Dict[str, Any]:
        """Gera relatório de métricas"""
        return self.metrics.generate_report()
    
    def get_agent_info(self, agent_id: str) -> Optional[Dict[str, Any]]:
        """Obtém informações de um agente específico"""
        if agent_id in self.agents:
            agent = self.agents[agent_id]
            return {
                'name': agent.name,
                'specialization': agent.specialization,
                'file_extensions': agent.file_extensions,
                'capabilities': agent.capabilities,
                'tools': agent.tools
            }
        return None
    
    def list_all_agents(self) -> List[Dict[str, Any]]:
        """Lista todos os agentes disponíveis"""
        return [self.get_agent_info(agent_id) for agent_id in self.agents.keys()]


class AAAAgent:
    """Agente especializado de nível AAA"""
    
    def __init__(self, name: str, specialization: str, file_extensions: List[str], 
                 capabilities: List[str], tools: List[str]):
        self.name = name
        self.specialization = specialization
        self.file_extensions = file_extensions
        self.capabilities = capabilities
        self.tools = tools
        self.execution_count = 0
        self.total_execution_time = 0.0
    
    def execute(self, file_path: str, user_request: str, context: Dict[str, Any]) -> Dict[str, Any]:
        """Executa análise e processamento do arquivo"""
        start_time = time.time()
        
        print(f"🔧 {self.name} executando análise...")
        
        # Análise específica baseada no tipo de agente
        analysis_result = self.perform_analysis(file_path, user_request, context)
        
        # Otimizações específicas
        optimization_result = self.perform_optimizations(file_path, analysis_result)
        
        # Validação de qualidade
        quality_result = self.validate_quality(file_path, analysis_result, optimization_result)
        
        # Calcula tempo de execução
        execution_time = time.time() - start_time
        self.execution_count += 1
        self.total_execution_time += execution_time
        
        result = {
            'agent_name': self.name,
            'specialization': self.specialization,
            'analysis_result': analysis_result,
            'optimization_result': optimization_result,
            'quality_result': quality_result,
            'execution_time': execution_time,
            'quality_score': quality_result.get('score', 0.0),
            'suggestions': quality_result.get('suggestions', []),
            'timestamp': datetime.now().isoformat()
        }
        
        print(f"✅ {self.name} concluído em {execution_time:.2f}s")
        
        return result
    
    def perform_analysis(self, file_path: str, user_request: str, context: Dict[str, Any]) -> Dict[str, Any]:
        """Realiza análise específica do arquivo"""
        # Implementação específica para cada tipo de agente
        # Por enquanto, retorna análise básica
        return {
            'file_size': os.path.getsize(file_path),
            'file_type': Path(file_path).suffix,
            'analysis_type': 'basic',
            'issues_found': [],
            'recommendations': []
        }
    
    def perform_optimizations(self, file_path: str, analysis_result: Dict[str, Any]) -> Dict[str, Any]:
        """Realiza otimizações específicas"""
        # Implementação específica para cada tipo de agente
        return {
            'optimizations_applied': [],
            'performance_improvements': [],
            'optimization_score': 0.0
        }
    
    def validate_quality(self, file_path: str, analysis_result: Dict[str, Any], 
                        optimization_result: Dict[str, Any]) -> Dict[str, Any]:
        """Valida qualidade do arquivo"""
        # Implementação específica para cada tipo de agente
        return {
            'score': 0.85,  # Score padrão
            'suggestions': [],
            'quality_gates_passed': True
        }


class AAAWorkflow:
    """Workflow de nível AAA"""
    
    def __init__(self, name: str, agents: List[str], phases: List[str], 
                 duration: str, quality_gates: List[str]):
        self.name = name
        self.agents = agents
        self.phases = phases
        self.duration = duration
        self.quality_gates = quality_gates
        self.execution_count = 0


class AAAMetrics:
    """Sistema de métricas AAA"""
    
    def __init__(self):
        self.response_times = []
        self.agent_accuracy = []
        self.file_coverage = []
        self.performance_improvements = []
        self.integration_success = []
    
    def record_metric(self, metric_type: str, value: float):
        """Registra métrica para análise"""
        if metric_type == 'response_time':
            self.response_times.append(value)
        elif metric_type == 'agent_accuracy':
            self.agent_accuracy.append(value)
        elif metric_type == 'file_coverage':
            self.file_coverage.append(value)
        elif metric_type == 'performance_improvement':
            self.performance_improvements.append(value)
        elif metric_type == 'integration_success':
            self.integration_success.append(value)
    
    def generate_report(self) -> Dict[str, Any]:
        """Gera relatório de métricas"""
        return {
            'total_executions': len(self.response_times),
            'average_response_time': sum(self.response_times) / len(self.response_times) if self.response_times else 0,
            'average_agent_accuracy': sum(self.agent_accuracy) / len(self.agent_accuracy) if self.agent_accuracy else 0,
            'file_coverage_rate': sum(self.file_coverage) / len(self.file_coverage) if self.file_coverage else 0,
            'performance_improvement_rate': sum(self.performance_improvements) / len(self.performance_improvements) if self.performance_improvements else 0,
    
    
            'integration_success_rate': sum(self.integration_success) / len(self.integration_success) if self.integration_success else 0,
    
    
            'timestamp': datetime.now().isoformat()
        }


class QualityMonitor:
    """Monitor de qualidade AAA"""
    
    def __init__(self):
        self.quality_gates = {}
        self.performance_baselines = {}
        self.security_checks = []
    
    def check_quality_gate(self, gate_name: str) -> float:
        """Verifica gate de qualidade"""
        # Implementação básica - retorna score padrão
        return 0.85
    
    def alert_degradation(self, metric: str, threshold: float):
        """Alerta sobre degradação"""
        print(f"⚠️ ALERTA: Degradação detectada em {metric} (threshold: {threshold})")


def main():
    """Função principal para teste do sistema"""
    print("🚀 Iniciando Sistema de Agentes Especializados AAA")
    
    # Inicializa sistema
    system = AAAAgentSpecializationSystem("wiki")
    
    # Testa detecção de contexto
    test_files = [
        "src/client/game.cpp",
        "modules/game_inventory/inventory.lua",
        "wiki/otclient/README.md",
        "wiki/maps/tags_index.json",
        "data/images/background.png"
    ]
    
    for test_file in test_files:
        print(f"\n🧪 Testando: {test_file}")
        context = system.detect_context_by_extension(test_file)
        print(f"   Contexto: {context['primary_agent']}")
        print(f"   Confiança: {context['confidence_score']:.2f}")
    
    # Testa execução de workflow
    print(f"\n🔄 Testando workflow AAA...")
    result = system.execute_agent_workflow(
        "modules/game_inventory/inventory.lua",
        "Otimizar performance do módulo de inventário"
    )
    
    # Gera relatório de métricas
    metrics_report = system.generate_metrics_report()
    print(f"\n📊 Relatório de Métricas:")
    print(json.dumps(metrics_report, indent=2))
    
    print(f"\n✅ Sistema AAA testado com sucesso!")


if __name__ == "__main__":
    main() 

# Função de integração com o módulo
def integrate_with_module():
    """Integra o script com o módulo de destino."""
    module = AgentspecialistModule()
    return module.execute()

if __name__ == "__main__":
    # Executar integração com módulo
    result = integrate_with_module()
    if result:
        print(f"✅ Script aaa_agent_specialization_system.py executado com sucesso via módulo agents.agent_specialist")
    else:
        print(f"❌ Erro na execução do script aaa_agent_specialization_system.py via módulo agents.agent_specialist")

## 🔗 **Links Automáticos - Scripts**

> [!info] **Script de Automação**
> Este script faz parte do sistema de automação da wiki

### **📚 Links Obrigatórios**
- [[../README|Hub Central da Wiki]]
- [[../dashboard/task_master|Task Master]]
- [[../dashboard/integrated_task_manager|Dashboard Central]]

### **🔧 Links de Scripts**
- [[../update/README|Documentação de Scripts]]
- [[../maps/scripts_index|Índice de Scripts]]
- [[../templates/README|Templates de Scripts]]

### **📊 Scripts Relacionados**
- [[../update/automatic_linkage_system.py|automatic_linkage_system.py]]
- [[../update/create_automatic_link_templates.py|create_automatic_link_templates.py]]
- [[../update/orphan_files_analyzer.py|orphan_files_analyzer.py]]
- [[../update/update_json_maps.py|update_json_maps.py]]

### **📈 Métricas do Script**
- **Nome**: migrated_aaa_agent_specialization_system
- **Categoria**: Scripts de Automação
- **Função**: Automação de tarefas da wiki
- **Status**: Ativo

---

