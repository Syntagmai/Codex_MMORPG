#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Intelligent Chat Integration - Integração Inteligente com Chat
=============================================================

Sistema que integra o criador inteligente de códigos com o chat,
permitindo criação baseada em conhecimento da wiki.

Autor: Sistema BMAD
Versão: 1.0.0
Data: 2025-01-27
"""

import sys
from pathlib import Path

# Adicionar pasta de agentes ao path
current_dir = Path(__file__).parent
agents_dir = current_dir
sys.path.insert(0, str(agents_dir))

try:
    from intelligent_code_creator import IntelligentCodeCreator
except ImportError as e:
    print(f"❌ Erro ao importar sistema: {e}")
    sys.exit(1)

# Instância global do sistema
_intelligent_creator = None

def get_intelligent_creator():
    """
    Obtém instância do criador inteligente.
    
    Returns:
        IntelligentCodeCreator: Instância do sistema
    """
    global _intelligent_creator
    if _intelligent_creator is None:
        _intelligent_creator = IntelligentCodeCreator()
    return _intelligent_creator

def create_intelligently(user_request: str) -> str:
    """
    Cria código de forma inteligente usando navegação wiki.
    
    Args:
        user_request: Pedido do usuário
        
    Returns:
        str: Resposta formatada do sistema
    """
    try:
        creator = get_intelligent_creator()
        result = creator.create_intelligently(user_request)
        
        if result['success']:
            return format_success_response(result)
        else:
            return format_error_response(result)
            
    except Exception as e:
        return f"❌ Erro ao processar criação: {str(e)}"

def format_success_response(result: dict) -> str:
    """Formata resposta de sucesso"""
    
    plan = result['plan']
    validation = result['validation']
    knowledge = result['knowledge_sources']
    
    response = f"""
🎯 **CRIAÇÃO INTELIGENTE CONCLUÍDA!**

📋 **PLANO EXECUTADO:**
- **Tipo**: {plan['request_type']}
- **Passos**: {len(plan['creation_steps'])} executados
- **Documentos consultados**: {len(knowledge['primary_docs'])}
- **Regras extraídas**: {len(knowledge['rules'])}
- **Padrões encontrados**: {len(knowledge['patterns'])}

📊 **VALIDAÇÃO:**
- **Score geral**: {validation['overall_score']:.1f}%
- **Regras aprovadas**: {len(validation['passed_rules'])}
- **Avisos**: {len(validation['warnings'])}

📚 **FONTES DE CONHECIMENTO:**
"""
    
    # Adicionar documentos consultados
    for doc in knowledge['primary_docs'][:5]:  # Mostrar apenas os 5 primeiros
        response += f"- {doc}\n"
    
    if len(knowledge['primary_docs']) > 5:
        response += f"- ... e mais {len(knowledge['primary_docs']) - 5} documentos\n"
    
    response += f"""
🔧 **RESULTADO:**
- **Arquivos criados**: {len(result['result']['files_created'])}
- **Código gerado**: {len(result['result']['code_generated'])} seções
- **Log de execução**: {len(result['result']['execution_log'])} passos

✅ **Sistema usado navegação wiki e planejamento inteligente!**
"""
    
    return response

def format_error_response(result: dict) -> str:
    """Formata resposta de erro"""
    
    return f"""
❌ **ERRO NA CRIAÇÃO INTELIGENTE**

🔍 **Problema identificado:**
{result['error']}

💡 **Sugestões:**
- Verifique se o pedido está claro
- Confirme se a documentação necessária existe na wiki
- Tente reformular o pedido com mais detalhes

📚 **Sistema tentou usar:**
- Navegação JSON da wiki
- Planejamento inteligente
- Extração de regras da documentação
"""

def analyze_request_intelligently(user_request: str) -> str:
    """
    Analisa pedido de forma inteligente sem executar criação.
    
    Args:
        user_request: Pedido do usuário
        
    Returns:
        str: Análise do pedido
    """
    try:
        creator = get_intelligent_creator()
        plan = creator.planner.create_plan(user_request)
        
        analysis = f"""
🔍 **ANÁLISE INTELIGENTE DO PEDIDO**

📝 **Pedido**: {user_request}

🎯 **Tipo identificado**: {plan.request_type}
📚 **Tópicos detectados**: {', '.join(plan.knowledge_sources.get('topics', []))}
📊 **Complexidade estimada**: {plan.knowledge_sources.get('complexity', 'unknown')}

📋 **PLANO PROPOSTO:**
"""
        
        for i, step in enumerate(plan.creation_steps, 1):
            analysis += f"{i}. {step}\n"
        
        analysis += f"""
📚 **CONHECIMENTO ENCONTRADO:**
- **Documentos primários**: {len(plan.knowledge_sources['primary_docs'])}
- **Documentos relacionados**: {len(plan.knowledge_sources['related_docs'])}
- **Regras extraídas**: {len(plan.knowledge_sources['rules'])}
- **Padrões identificados**: {len(plan.knowledge_sources['patterns'])}

✅ **Sistema está pronto para criar usando conhecimento da wiki!**
"""
        
        return analysis
        
    except Exception as e:
        return f"❌ Erro na análise: {str(e)}"

def get_creation_statistics() -> str:
    """
    Obtém estatísticas do sistema de criação.
    
    Returns:
        str: Estatísticas formatadas
    """
    try:
        creator = get_intelligent_creator()
        
        # Simular estatísticas (em implementação real, seria baseado em histórico)
        stats = {
            'total_creations': 0,
            'successful_creations': 0,
            'average_score': 0.0,
            'knowledge_sources_used': 0,
            'rules_extracted': 0
        }
        
        return f"""
📊 **ESTATÍSTICAS DO SISTEMA INTELIGENTE**

🎯 **Criações realizadas**: {stats['total_creations']}
✅ **Sucessos**: {stats['successful_creations']}
📊 **Score médio**: {stats['average_score']:.1f}%
📚 **Fontes de conhecimento usadas**: {stats['knowledge_sources_used']}
📋 **Regras extraídas**: {stats['rules_extracted']}

🔧 **Sistema ativo e pronto para uso!**
"""
        
    except Exception as e:
        return f"❌ Erro ao obter estatísticas: {str(e)}"

def show_available_commands() -> str:
    """
    Mostra comandos disponíveis.
    
    Returns:
        str: Lista de comandos
    """
    return """
🎯 **COMANDOS DO SISTEMA INTELIGENTE**

📝 **Criação:**
- `create_intelligently("criar um módulo de inventário")`
- `create_intelligently("criar uma magia de fogo para Canary")`
- `create_intelligently("criar uma interface modal")`

🔍 **Análise:**
- `analyze_request_intelligently("pedido do usuário")`

📊 **Estatísticas:**
- `get_creation_statistics()`

💡 **Como funciona:**
1. **Análise inteligente** do pedido
2. **Navegação wiki** usando mapas JSON
3. **Extração de regras** da documentação
4. **Planejamento detalhado** antes da criação
5. **Validação** usando regras extraídas
6. **Resultado** baseado em conhecimento real

✅ **Não adivinha - usa documentação como fonte única de verdade!**
"""

def test_system():
    """Testa o sistema"""
    print("🧠 Testando Sistema Inteligente de Criação...")
    
    test_requests = [
        "criar um módulo de inventário para OTClient",
        "criar uma magia de fogo para Canary",
        "criar uma interface modal para OTClient"
    ]
    
    for request in test_requests:
        print(f"\n{'='*60}")
        print(f"TESTANDO: {request}")
        print(f"{'='*60}")
        
        # Testar análise
        analysis = analyze_request_intelligently(request)
        print(analysis)
        
        # Testar criação
        result = create_intelligently(request)
        print(result)

if __name__ == "__main__":
    test_system() 