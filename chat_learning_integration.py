#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Chat Learning Integration - Integração do Sistema de Aprendizado com IA do Chat
===============================================================================

Sistema que permite que a IA do chat use o sistema de aprendizado inteligente
diretamente, entendendo comandos naturais e executando workflows automaticamente.

Uso pela IA:
- process_chat_command("criar um módulo de inventário")
- process_chat_command("@analyze network patterns")
- process_chat_command("aprender sobre tratamento de erros")

Autor: Sistema BMAD
Versão: 1.0.0
Data: 2025-01-27
"""

import sys
from pathlib import Path

# Adicionar pasta de agentes ao path
current_dir = Path(__file__).parent
agents_dir = current_dir / "wiki" / "bmad" / "agents"
sys.path.insert(0, str(agents_dir))

try:
    from intelligent_chat_learning_system import IntelligentChatLearningSystem
except ImportError as e:
    print(f"❌ Erro ao importar sistema: {e}")
    sys.exit(1)

# Instância global do sistema
_learning_system = None

def get_learning_system():
    """
    Obtém instância do sistema de aprendizado.
    
    Returns:
        IntelligentChatLearningSystem: Instância do sistema
    """
    global _learning_system
    if _learning_system is None:
        _learning_system = IntelligentChatLearningSystem()
    return _learning_system

def process_chat_command(user_message: str) -> str:
    """
    Processa comando do chat usando o sistema de aprendizado inteligente.
    
    Args:
        user_message: Mensagem do usuário
        
    Returns:
        str: Resposta do sistema
    """
    try:
        system = get_learning_system()
        return system.process_chat_message(user_message)
    except Exception as e:
        return f"❌ Erro ao processar comando: {str(e)}"

def create_module_intelligently(module_description: str) -> str:
    """
    Cria módulo de forma inteligente.
    
    Args:
        module_description: Descrição do módulo
        
    Returns:
        str: Resposta do processo de criação
    """
    try:
        system = get_learning_system()
        return system.create_module_intelligently(module_description)
    except Exception as e:
        return f"❌ Erro ao criar módulo: {str(e)}"

def analyze_pattern_intelligently(pattern_description: str) -> str:
    """
    Analisa padrão de forma inteligente.
    
    Args:
        pattern_description: Descrição do padrão
        
    Returns:
        str: Resposta da análise
    """
    try:
        system = get_learning_system()
        return system.analyze_pattern_intelligently(pattern_description)
    except Exception as e:
        return f"❌ Erro ao analisar padrão: {str(e)}"

def learn_about_topic(topic: str) -> str:
    """
    Aprende sobre um tópico específico.
    
    Args:
        topic: Tópico para aprender
        
    Returns:
        str: Resposta do aprendizado
    """
    try:
        system = get_learning_system()
        return system.learn_about_topic(topic)
    except Exception as e:
        return f"❌ Erro ao aprender sobre tópico: {str(e)}"

def improve_existing_code(target: str) -> str:
    """
    Melhora código existente.
    
    Args:
        target: Alvo para melhoria
        
    Returns:
        str: Resposta da melhoria
    """
    try:
        system = get_learning_system()
        return system.improve_existing_code(target)
    except Exception as e:
        return f"❌ Erro ao melhorar código: {str(e)}"

def get_learning_statistics() -> dict:
    """
    Obtém estatísticas de aprendizado.
    
    Returns:
        dict: Estatísticas de aprendizado
    """
    try:
        system = get_learning_system()
        return system.get_learning_statistics()
    except Exception as e:
        return {"error": f"Erro ao obter estatísticas: {str(e)}"}

def show_available_commands() -> str:
    """
    Mostra comandos disponíveis.
    
    Returns:
        str: Lista de comandos disponíveis
    """
    return """
🧠 **Sistema de Aprendizado Inteligente - Comandos Disponíveis**

📖 **Comandos Diretos:**
• @create "módulo" - Criar novo módulo
• @analyze "padrão" - Analisar padrão de código
• @learn "tópico" - Aprender sobre tópico
• @improve "código" - Melhorar código existente
• @study "padrão" - Estudar padrão específico
• @compare "padrão1" with "padrão2" - Comparar padrões
• @optimize "código" - Otimizar código
• @document "módulo" - Documentar módulo

💬 **Comandos Naturais:**
• "criar um módulo de inventário"
• "analisar padrões de rede"
• "aprender sobre tratamento de erros"
• "melhorar componentes de interface"
• "estudar como o OTClient funciona"
• "otimizar código de performance"

📝 **Exemplos de Uso:**
• @create "inventory system"
• @analyze "network patterns"
• @learn "error handling"
• @improve "ui components"
• "criar um sistema de inventário"
• "analisar como o OTClient trata conexões"

🎯 **Funcionalidades:**
• Análise inteligente de código existente
• Criação baseada em padrões aprendidos
• Comentários e documentação automática
• Avaliação de qualidade
• Aprendizado contínuo
• Memória persistente de conhecimento

🔄 **Workflow Automático:**
1. Análise do código de referência
2. Geração baseada em aprendizado
3. Análise educacional e comentários
4. Avaliação de qualidade
5. Documentação e feedback
6. Atualização da memória de aprendizado
"""

def test_system():
    """Testa o sistema de integração."""
    print("🧠 Testando Sistema de Integração\n")
    
    test_commands = [
        '@create "inventory system"',
        '@analyze "network patterns"',
        '@learn "error handling"',
        'criar um módulo de inventário',
        'analisar padrões de rede',
        'aprender sobre tratamento de erros'
    ]
    
    for command in test_commands:
        print(f"📝 Testando: {command}")
        response = process_chat_command(command)
        print(response[:200] + "..." if len(response) > 200 else response)
        print("-" * 50)

if __name__ == "__main__":
    test_system() 