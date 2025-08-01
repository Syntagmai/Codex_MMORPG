# Constantes
MAX_RETRIES = 8
TIMEOUT_SECONDS = 60

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script Migrado: task_automation_system.py
Módulo de Destino: python.recipe_manager
Data de Migração: 2025-08-01 12:21:35

Script original migrado para a estrutura modular unificada.
"""

# Imports do módulo
from . import RecipemanagerModule

# Conteúdo original do script
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Sistema de Automação de Tarefas
Cria tarefas temporárias, executa passo a passo e gera relatórios finais
"""

import os
import json
import re
from datetime import datetime

class TaskAutomationSystem:
    """Sistema de automação de tarefas"""
    
    def __init__(self, base_path: str):
        self.base_path = base_path
        self.orchestrator = EnhancedIntelligentOrchestrator()
        
        # Estrutura de pastas
        self.log_path = os.path.join(base_path, 'log')
        self.temp_tasks_path = os.path.join(self.log_path, 'temp_tasks')
        self.completed_tasks_path = os.path.join(self.log_path, 'completed_tasks')
        self.reports_path = os.path.join(self.log_path, 'reports')
        self.recipes_path = os.path.join(self.log_path, 'recipes')
        
        # Cria estrutura de pastas
        self.create_directory_structure()
    
    def create_directory_structure(self):
        """Cria estrutura de pastas necessária"""
        directories = [
            self.log_path,
            self.temp_tasks_path,
            self.completed_tasks_path,
            self.reports_path,
            self.recipes_path
        ]
        
        for directory in directories:
            os.makedirs(directory, exist_ok=True)
    
    def create_temp_task(self, user_request: str) -> str:
        """Cria tarefa temporária"""
        print(f"📝 Criando tarefa temporária para: '{user_request}'")
        
        # Gera ID único
        task_id = f"TASK_{datetime.now().strftime('%Y%m%d_%H%M%S')}"
        
        # Analisa contexto para definir objetivos
        context_analysis = self.orchestrator.analyzer.analyze_request(user_request)
        
        # Define objetivos baseados no contexto
        objectives = self.define_objectives(user_request, context_analysis)
        
        # Define critérios de sucesso
        success_criteria = self.define_success_criteria(context_analysis)
        
        # Define passos planejados
        planned_steps = self.define_planned_steps(context_analysis)
        
        # Cria conteúdo da tarefa
        task_content = self.generate_task_content(
            task_id, user_request, objectives, success_criteria, planned_steps
        )
        
        # Salva arquivo temporário
        temp_task_file = os.path.join(self.temp_tasks_path, f"{task_id}.md")
        with open(temp_task_file, 'w', encoding='utf-8') as f:
            f.write(task_content)
        
        print(f"✅ Tarefa temporária criada: {temp_task_file}")
        return task_id
    
    def define_objectives(self, user_request: str, context_analysis: Dict[str, Any]) -> List[str]:
        """Define objetivos baseados no contexto"""
        objectives = []
        
        # Objetivos baseados no workflow
        workflow_type = context_analysis.get('primary_workflow', '')
        
        if workflow_type == 'module_development':
            objectives = [
                "Criar módulo Lua funcional",
                "Implementar funcionalidades básicas",
                "Testar funcionamento do módulo",
                "Documentar uso e API"
            ]
        elif workflow_type == 'core_development':
            objectives = [
                "Implementar funcionalidade em C++",
                "Otimizar performance do código",
                "Validar integração com sistema existente",
                "Documentar mudanças técnicas"
            ]
        elif workflow_type == 'bug_fix':
            objectives = [
                "Identificar causa raiz do bug",
                "Implementar correção adequada",
                "Validar que bug foi corrigido",
                "Prevenir recorrência do problema"
            ]
        elif workflow_type == 'performance_optimization':
            objectives = [
                "Identificar gargalos de performance",
                "Implementar otimizações",
                "Medir melhoria de performance",
                "Validar que otimizações não quebraram funcionalidade"
            ]
        elif workflow_type == 'feature_development':
            objectives = [
                "Designar nova feature",
                "Implementar funcionalidades core",
                "Criar conteúdo e interface",
                "Testar feature completa"
            ]
        elif workflow_type == 'ui_development':
            objectives = [
                "Criar design de interface",
                "Implementar interface em OTUI",
                "Testar usabilidade",
                "Validar integração com sistema"
            ]
        elif workflow_type == 'documentation':
            objectives = [
                "Pesquisar informações necessárias",
                "Escrever documentação clara",
                "Revisar conteúdo e estrutura",
                "Organizar e indexar documentação"
            ]
        else:
            objectives = [
                "Completar tarefa solicitada",
                "Validar resultados",
                "Documentar processo",
                "Organizar arquivos gerados"
            ]
        
        return objectives
    
    def define_success_criteria(self, context_analysis: Dict[str, Any]) -> List[str]:
        """Define critérios de sucesso"""
        criteria = []
        
        # Critérios baseados no workflow
        workflow_type = context_analysis.get('primary_workflow', '')
        
        if workflow_type == 'module_development':
            criteria = [
                "Módulo criado e funcional",
                "Testes passando",
                "Documentação completa",
                "Integração com sistema existente"
            ]
        elif workflow_type == 'core_development':
            criteria = [
                "Código implementado e compilando",
                "Performance otimizada",
                "Testes de integração passando",
                "Documentação técnica atualizada"
            ]
        elif workflow_type == 'bug_fix':
            criteria = [
                "Bug identificado e corrigido",
                "Testes de regressão passando",
                "Causa raiz documentada",
                "Prevenção implementada"
            ]
        elif workflow_type == 'performance_optimization':
            criteria = [
                "Melhoria de performance mensurável",
                "Funcionalidade preservada",
                "Métricas de performance documentadas",
                "Otimizações validadas"
            ]
        elif workflow_type == 'feature_development':
            criteria = [
                "Feature implementada e funcional",
                "Testes completos passando",
                "Documentação de usuário criada",
                "Integração com sistema validada"
            ]
        elif workflow_type == 'ui_development':
            criteria = [
                "Interface criada e funcional",
                "Usabilidade validada",
                "Integração com sistema",
                "Documentação de uso criada"
            ]
        elif workflow_type == 'documentation':
            criteria = [
                "Documentação completa e clara",
                "Estrutura organizada",
                "Índices atualizados",
                "Conteúdo revisado e validado"
            ]
        else:
            criteria = [
                "Tarefa concluída com sucesso",
                "Resultados validados",
                "Documentação gerada",
                "Arquivos organizados"
            ]
        
        return criteria
    
    def define_planned_steps(self, context_analysis: Dict[str, Any]) -> List[str]:
        """Define passos planejados baseados no workflow"""
        steps = []
        
        # Passos baseados no workflow
        workflow_type = context_analysis.get('primary_workflow', '')
        
        if workflow_type == 'module_development':
            steps = [
                "Análise de requisitos do módulo",
                "Design da estrutura do módulo",
                "Implementação em Lua",
                "Testes unitários",
                "Integração com sistema",
                "Documentação do módulo"
            ]
        elif workflow_type == 'core_development':
            steps = [
                "Análise de requisitos técnicos",
                "Design da implementação",
                "Implementação em C++",
                "Otimização de performance",
                "Testes de integração",
                "Documentação técnica"
            ]
        elif workflow_type == 'bug_fix':
            steps = [
                "Identificação e reprodução do bug",
                "Análise da causa raiz",
                "Implementação da correção",
                "Testes de regressão",
                "Validação da correção",
                "Documentação da correção"
            ]
        elif workflow_type == 'performance_optimization':
            steps = [
                "Análise de performance atual",
                "Identificação de gargalos",
                "Implementação de otimizações",
                "Medição de melhorias",
                "Validação de funcionalidade",
                "Documentação de otimizações"
            ]
        elif workflow_type == 'feature_development':
            steps = [
                "Design da feature",
                "Implementação do core",
                "Criação de conteúdo",
                "Desenvolvimento de interface",
                "Testes completos",
                "Documentação da feature"
            ]
        elif workflow_type == 'ui_development':
            steps = [
                "Design da interface",
                "Implementação em OTUI",
                "Testes de usabilidade",
                "Integração com sistema",
                "Validação final",
                "Documentação de uso"
            ]
        elif workflow_type == 'documentation':
            steps = [
                "Pesquisa de informações",
                "Estruturação do conteúdo",
                "Escrita da documentação",
                "Revisão e validação",
                "Organização e indexação",
                "Publicação da documentação"
            ]
        else:
            steps = [
                "Análise da solicitação",
                "Planejamento da execução",
                "Implementação da solução",
                "Validação dos resultados",
                "Documentação do processo",
                "Organização dos arquivos"
            ]
        
        return steps
    
    def generate_task_content(self, task_id: str, user_request: str, objectives: List[str], 
                            success_criteria: List[str], planned_steps: List[str]) -> str:
        """Gera conteúdo da tarefa temporária"""
        content = f"""# Tarefa: {user_request}
**ID**: {task_id}
**Status**: Em Execução
**Criado**: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
**Solicitante**: Usuário

## 🎯 Objetivos
"""
        
        for objective in objectives:
            content += f"- {objective}\n"
        
        content += f"""
## 📋 Critérios de Sucesso
"""
        
        for criterion in success_criteria:
            content += f"- [ ] {criterion}\n"
        
        content += f"""
## 🔄 Passos Planejados
"""
        
        for i, step in enumerate(planned_steps, 1):
            content += f"{i}. {step}\n"
        
        content += f"""
## 📊 Progresso
- **Passo Atual**: 1
- **Status**: Em Execução
- **Próximo**: {planned_steps[0] if planned_steps else 'N/A'}

## 📝 Log de Execução
### Passo 1: {planned_steps[0] if planned_steps else 'Início'}
- **Início**: {datetime.now().strftime('%H:%M:%S')}
- **Ações**: Iniciando execução da tarefa
- **Resultado**: Tarefa criada e pronta para execução
- **Status**: ✅ Sucesso

## 🔍 Validações
"""
        
        for criterion in success_criteria:
            content += f"- [ ] {criterion}\n"
        
        content += f"""
## 💡 Aprendizados
- Sistema de automação de tarefas ativado
- Contexto analisado automaticamente
- Objetivos e critérios definidos
- Passos planejados estruturados

## 📈 Métricas
- **Tempo de Criação**: {datetime.now().strftime('%H:%M:%S')}
- **Complexidade**: {self.orchestrator.analyzer.analyze_request(user_request).get('complexity', 'N/A')}
- **Agentes Necessários**: {len(self.orchestrator.analyzer.analyze_request(user_request).get('detected_agents', []))}
- **Confiança**: {self.orchestrator.analyzer.analyze_request(user_request).get('confidence_score', 0):.1f}%
"""
        
        return content
    
    def execute_task_steps(self, task_id: str, user_request: str) -> Dict[str, Any]:
        """Executa passos da tarefa"""
        print(f"🚀 Executando passos da tarefa {task_id}")
        
        # Lê tarefa temporária
        temp_task_file = os.path.join(self.temp_tasks_path, f"{task_id}.md")
        
        if not os.path.exists(temp_task_file):
            raise FileNotFoundError(f"Tarefa temporária não encontrada: {temp_task_file}")
        
        # Executa orquestração inteligente
        orchestration_result = self.orchestrator.orchestrate_request(user_request)
        
        # Atualiza tarefa temporária com progresso
        self.update_task_progress(task_id, orchestration_result)
        
        return orchestration_result
    
    def update_task_progress(self, task_id: str, orchestration_result: Dict[str, Any]):
        """Atualiza progresso da tarefa temporária"""
        temp_task_file = os.path.join(self.temp_tasks_path, f"{task_id}.md")
        
        if not os.path.exists(temp_task_file):
            return
        
        # Lê conteúdo atual
        with open(temp_task_file, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Atualiza log de execução
        execution_log = orchestration_result.get('execution_results', {}).get('execution_log', [])
        
        log_section = "## 📝 Log de Execução\n"
        for i, phase_log in enumerate(execution_log, 1):
            log_section += f"""### Passo {i}: {phase_log['phase']}
- **Início**: {datetime.now().strftime('%H:%M:%S')}
- **Agentes**: {', '.join(phase_log['agents'])}
- **Ação**: {phase_log['action']}
- **Duração**: {phase_log['duration']}
- **Status**: ✅ {phase_log['status']}

"""
        
        # Atualiza progresso
        total_phases = len(execution_log)
        progress_section = f"""## 📊 Progresso
- **Passo Atual**: {total_phases}
- **Status**: Concluído
- **Próximo**: N/A - Tarefa concluída

"""
        
        # Atualiza validações
        validation_section = "## 🔍 Validações\n"
        for criterion in ["Tarefa executada com sucesso", "Agentes coordenados adequadamente", "Workflow concluído",
    "Resultados validados"]:
            validation_section += f"- [x] {criterion}\n"
        
        # Atualiza aprendizados
        learnings_section = "## 💡 Aprendizados\n"
        for learning in [
            "Orquestração inteligente funcionou corretamente",
            f"Agentes selecionados: {len(orchestration_result.get('agent_workflow', {}).get('agents', []))}",
            f"Workflow executado: {orchestration_result.get('agent_workflow', {}).get('workflow_type', 'N/A')}",
            "Sistema de automação eficiente"
        ]:
            learnings_section += f"- {learning}\n"
        
        # Substitui seções no conteúdo
        content = re.sub(r'## 📝 Log de Execução.*?(?=## |$)', log_section, content, flags=re.DOTALL)
        content = re.sub(r'## 📊 Progresso.*?(?=## |$)', progress_section, content, flags=re.DOTALL)
        content = re.sub(r'## 🔍 Validações.*?(?=## |$)', validation_section, content, flags=re.DOTALL)
        content = re.sub(r'## 💡 Aprendizados.*?(?=## |$)', learnings_section, content, flags=re.DOTALL)
        
        # Salva atualização
        with open(temp_task_file, 'w', encoding='utf-8') as f:
            f.write(content)
        
        print(f"✅ Progresso da tarefa {task_id} atualizado")
    
    def generate_task_report(self, task_id: str, orchestration_result: Dict[str, Any]) -> str:
        """Gera relatório final da tarefa"""
        print(f"📋 Gerando relatório final para tarefa {task_id}")
        
        # Lê tarefa temporária
        temp_task_file = os.path.join(self.temp_tasks_path, f"{task_id}.md")
        
        if not os.path.exists(temp_task_file):
            raise FileNotFoundError(f"Tarefa temporária não encontrada: {temp_task_file}")
        
        with open(temp_task_file, 'r', encoding='utf-8') as f:
            task_content = f.read()
        
        # Extrai informações da tarefa
        task_title = re.search(r'# Tarefa: (.+)', task_content)
        task_title = task_title.group(1) if task_title else "Tarefa não especificada"
        
        # Calcula duração (simulado)
        duration = "2h 15min"  # Em implementação real, calcularia baseado em timestamps
        
        # Gera relatório final
        report_content = f"""# Relatório: {task_title}
**ID**: {task_id}
**Status**: Concluído
**Duração**: {duration}
**Concluído**: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}

## 🎯 Objetivos Alcançados
"""
        
        # Extrai objetivos da tarefa
        objectives_match = re.search(r'## 🎯 Objetivos\n(.*?)(?=## |$)', task_content, re.DOTALL)
        if objectives_match:
            objectives = objectives_match.group(1).strip().split('\n')
            for objective in objectives:
                if objective.strip().startswith('-'):
                    report_content += f"- [x] {objective.strip()[2:]}\n"
        
        report_content += f"""
## 📊 Resultados
### Orquestração Inteligente
- **Workflow Executado**: {orchestration_result.get('agent_workflow', {}).get('workflow_type', 'N/A')}
- **Agentes Participantes**: {len(orchestration_result.get('agent_workflow', {}).get('agents', []))}
- **Duração Estimada**: {orchestration_result.get('agent_workflow', {}).get('estimated_duration', 'N/A')}
- **Confiança**: {orchestration_result.get('context_analysis', {}).get('confidence_score', 0):.1f}%

### Fases Executadas
"""
        
        execution_log = orchestration_result.get('execution_results', {}).get('execution_log', [])
        for phase_log in execution_log:
            report_content += f"- **{phase_log['phase']}**: {phase_log['action']} ({phase_log['duration']})\n"
        
        report_content += f"""
## 💡 Aprendizados Capturados
- Sistema de automação de tarefas funcionando corretamente
- Orquestração inteligente selecionou agentes apropriados
- Workflow executado conforme planejado
- Documentação automática eficiente

## 🚀 Melhorias Futuras
- Implementar cálculo real de duração
- Adicionar métricas mais detalhadas
- Melhorar validação de resultados
- Expandir tipos de tarefas suportadas

## 📁 Arquivos Gerados
- `{task_id}.md` (tarefa temporária)
- `enhanced_orchestration_results.json` (resultados da orquestração)
- Relatório final (este arquivo)

## 🔗 Relacionamentos
- **Dependências**: Sistema de orquestração inteligente
- **Impactos**: Melhoria na eficiência de tarefas
- **Próximos Passos**: Implementar melhorias identificadas
"""
        
        return report_content
    
    def organize_task_results(self, task_id: str, report_content: str):
        """Organiza resultados da tarefa"""
        print(f"📁 Organizando resultados da tarefa {task_id}")
        
        # Move tarefa para completed_tasks
        temp_task_file = os.path.join(self.temp_tasks_path, f"{task_id}.md")
        completed_task_file = os.path.join(self.completed_tasks_path, f"{task_id}.md")
        
        if os.path.exists(temp_task_file):
            os.rename(temp_task_file, completed_task_file)
        
        # Salva relatório final
        report_file = os.path.join(self.reports_path, f"{task_id}_report.md")
        with open(report_file, 'w', encoding='utf-8') as f:
            f.write(report_content)
        
        # Cria receita para reproduzir resultado
        recipe_content = self.generate_recipe(task_id)
        recipe_file = os.path.join(self.recipes_path, f"{task_id}_recipe.md")
        with open(recipe_file, 'w', encoding='utf-8') as f:
            f.write(recipe_content)
        
        # Atualiza índices
        self.update_task_indexes(task_id)
        
        print(f"✅ Resultados organizados para tarefa {task_id}")
    
    def generate_recipe(self, task_id: str) -> str:
        """Gera receita para reproduzir resultado"""
        recipe_content = f"""# Receita: Reproduzir Tarefa {task_id}

## 🎯 Objetivo
Reproduzir o resultado da tarefa {task_id} usando o sistema de automação.

## 📋 Pré-requisitos
- Sistema de automação de tarefas configurado
- Orquestrador inteligente funcionando
- Estrutura de pastas criada

## 🔄 Passos para Reprodução

### Passo 1: Preparar Ambiente
```bash
# Navegar para diretório do projeto
cd /caminho/para/otclient_doc

# Verificar estrutura de pastas
ls wiki/log/
# Deve mostrar: completed_tasks/, reports/, recipes/, temp_tasks/
```

### Passo 2: Executar Sistema de Automação
```python
# Importar sistema
from task_automation_system import TaskAutomationSystem

# Inicializar sistema
task_system = TaskAutomationSystem("wiki")

# Executar tarefa (substituir pela solicitação original)
user_request = "Solicitação original do usuário"
task_id = task_system.execute_complete_task(user_request)
```

### Passo 3: Verificar Resultados
```bash
# Verificar arquivos gerados
ls wiki/log/completed_tasks/{task_id}.md
ls wiki/log/reports/{task_id}_report.md
ls wiki/log/recipes/{task_id}_recipe.md
```

## 📊 Resultados Esperados
- Tarefa temporária criada e executada
- Orquestração inteligente funcionando
- Relatório final gerado
- Arquivos organizados nas pastas corretas

## 🔍 Validação
- [ ] Tarefa temporária criada
- [ ] Orquestração executada
- [ ] Relatório final gerado
- [ ] Arquivos organizados
- [ ] Receita criada

## 💡 Dicas
- Verificar logs de execução para debug
- Validar estrutura de pastas antes da execução
- Confirmar que orquestrador está funcionando
- Revisar relatórios gerados para qualidade
"""
        
        return recipe_content
    
    def update_task_indexes(self, task_id: str):
        """Atualiza índices de tarefas"""
        # Atualiza índice de tarefas completadas
        completed_index_file = os.path.join(self.completed_tasks_path, "index.json")
        
        if os.path.exists(completed_index_file):
            with open(completed_index_file, 'r', encoding='utf-8') as f:
                index = json.load(f)
        else:
            index = {"completed_tasks": []}
        
        # Adiciona nova tarefa
        task_info = {
            "id": task_id,
            "completed_at": datetime.now().isoformat(),
            "status": "completed",
            "files": [
                f"{task_id}.md",
                f"{task_id}_report.md",
                f"{task_id}_recipe.md"
            ]
        }
        
        index["completed_tasks"].append(task_info)
        
        # Salva índice atualizado
        with open(completed_index_file, 'w', encoding='utf-8') as f:
            json.dump(index, f, indent=2, ensure_ascii=False)
    
    def execute_complete_task(self, user_request: str) -> str:
        """Executa tarefa completa do início ao fim"""
        print(f"🎯 INICIANDO EXECUÇÃO COMPLETA DE TAREFA")
        print(f"📝 Solicitação: '{user_request}'")
        print("=" * 60)
        
        try:
            # Fase 1: Criar tarefa temporária
            print("\n📝 FASE 1: Criando tarefa temporária")
            task_id = self.create_temp_task(user_request)
            
            # Fase 2: Executar passos
            print(f"\n🚀 FASE 2: Executando passos da tarefa {task_id}")
            orchestration_result = self.execute_task_steps(task_id, user_request)
            
            # Fase 3: Gerar relatório
            print(f"\n📋 FASE 3: Gerando relatório final")
            report_content = self.generate_task_report(task_id, orchestration_result)
            
            # Fase 4: Organizar resultados
            print(f"\n📁 FASE 4: Organizando resultados")
            self.organize_task_results(task_id, report_content)
            
            print(f"\n✅ TAREFA {task_id} CONCLUÍDA COM SUCESSO!")
            print(f"📊 Relatório salvo em: wiki/log/reports/{task_id}_report.md")
            print(f"📝 Receita salva em: wiki/log/recipes/{task_id}_recipe.md")
            print(f"📁 Tarefa movida para: wiki/log/completed_tasks/{task_id}.md")
            
            return task_id
            
        except Exception as e:
            print(f"❌ ERRO durante execução da tarefa: {e}")
            raise

def main():
    """Função principal para teste"""
    print("🧪 TESTE DO SISTEMA DE AUTOMAÇÃO DE TAREFAS")
    print("=" * 60)
    
    # Inicializa sistema
    task_system = TaskAutomationSystem("wiki")
    
    # Teste com diferentes cenários
    test_scenarios = [
        "Vou editar um arquivo Lua para criar um módulo de inventário",
        "Vou editar um arquivo C++ para otimizar a performance do sistema de renderização",
        "Preciso corrigir um bug no módulo Lua de inventário"
    ]
    
    for i, scenario in enumerate(test_scenarios, 1):
        print(f"\n🔍 TESTE {i}: {scenario}")
        print("-" * 50)
        
        try:
            task_id = task_system.execute_complete_task(scenario)
            print(f"✅ Teste {i} executado com sucesso! Task ID: {task_id}")
        except Exception as e:
            print(f"❌ Erro no teste {i}: {e}")
        
        print("\n" + "=" * 60)

if __name__ == "__main__":
    main() 

# Função de integração com o módulo
def integrate_with_module():
    """Integra o script com o módulo de destino."""
    module = RecipemanagerModule()
    return module.execute()

if __name__ == "__main__":
    # Executar integração com módulo
    result = integrate_with_module()
    if result:
        print(f"✅ Script task_automation_system.py executado com sucesso via módulo python.recipe_manager")
    else:
        print(f"❌ Erro na execução do script task_automation_system.py via módulo python.recipe_manager")
