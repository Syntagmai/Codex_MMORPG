#!/usr/bin/env python3
"""
Script para processar e otimizar exemplos de código na wiki.
Adiciona comentários, divide blocos longos e melhora a estrutura.
"""
import os
import re
import json
from datetime import datetime
from pathlib import Path

def optimize_code_examples():
    """Otimiza exemplos de código na wiki."""
    
    wiki_path = Path("wiki")
    analysis_file = Path("wiki/maps/code_examples_analysis.json")
    
    if not analysis_file.exists():
        print("❌ Arquivo de análise não encontrado!")
        return
    
    # Carregar análise
    with open(analysis_file, 'r', encoding='utf-8') as f:
        analysis_data = json.load(f)
    
    # Focar nos arquivos principais
    main_files = [
        "docs/otclient/guides/Module_Development_Guide.md",
        "Troubleshooting_Comum.md"
    ]
    
    optimizations_applied = []
    
    print(f"🔧 Otimizando exemplos de código em {len(main_files)} arquivos...")
    
    for file_name in main_files:
        file_path = wiki_path / file_name
        
        if not file_path.exists():
            print(f"⚠️ Arquivo não encontrado: {file_name}")
            continue
        
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            original_content = content
            file_optimizations = []
            
            # Otimizar blocos de código
            content = optimize_code_blocks(content, file_name, analysis_data, file_optimizations)
            
            # Salvar se houve mudanças
            if content != original_content:
                with open(file_path, 'w', encoding='utf-8') as f:
                    f.write(content)
                
                optimizations_applied.append({
                    "file": file_name,
                    "optimizations": file_optimizations
                })
                
                print(f"✅ {file_name}: {len(file_optimizations)} otimizações aplicadas")
            else:
                print(f"⏭️ {file_name}: Nenhuma otimização necessária")
                
        except Exception as e:
            print(f"❌ Erro ao processar {file_name}: {e}")
    
    # Salvar relatório de otimizações
    report_data = {
        "metadata": {
            "optimization_date": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "files_processed": len(main_files),
            "files_optimized": len(optimizations_applied),
            "total_optimizations": sum(len(f["optimizations"]) for f in optimizations_applied)
        },
        "optimizations_applied": optimizations_applied
    }
    
    report_file = Path("wiki/maps/code_examples_optimization_report.json")
    with open(report_file, 'w', encoding='utf-8') as f:
        json.dump(report_data, f, indent=2, ensure_ascii=False)
    
    print(f"\n✅ Otimização concluída!")
    print(f"📊 Arquivos processados: {len(main_files)}")
    print(f"🔧 Arquivos otimizados: {len(optimizations_applied)}")
    print(f"✨ Total de otimizações: {sum(len(f['optimizations']) for f in optimizations_applied)}")
    print(f"📋 Relatório salvo: {report_file}")
    
    return report_data

def optimize_code_blocks(content, file_name, analysis_data, file_optimizations):
    """Otimiza blocos de código no conteúdo."""
    
    # Encontrar blocos que precisam de otimização
    blocks_to_optimize = [
        block for block in analysis_data["code_blocks"] 
        if block["file"] == file_name and block["needs_optimization"]
    ]
    
    for block_info in blocks_to_optimize:
        # Aplicar otimizações específicas
        if block_info["lines_count"] > 50:
            content = split_long_code_block(content, block_info, file_optimizations)
        
        if not block_info["has_comments"]:
            content = add_comments_to_code_block(content, block_info, file_optimizations)
    
    return content

def split_long_code_block(content, block_info, file_optimizations):
    """Divide blocos de código longos em partes menores."""
    
    # Padrão para encontrar o bloco específico
    pattern = r'```(\w+)?\n(.*?)```'
    
    def replace_block(match):
        language = match.group(1) or ''
        code_content = match.group(2)
        
        # Verificar se é o bloco que queremos dividir
        if len(code_content.split('\n')) > 50:
            # Dividir o código em partes lógicas
            parts = split_code_logically(code_content, language)
            
            # Criar novo conteúdo dividido
            new_content = ""
            for i, part in enumerate(parts):
                new_content += f"```{language}\n{part}\n```\n\n"
            
            file_optimizations.append({
                "type": "split_long_block",
                "description": f"Dividido bloco de {len(code_content.split('\n'))} linhas em {len(parts)} partes",
                "language": language
            })
            
            return new_content
        
        return match.group(0)
    
    return re.sub(pattern, replace_block, content, flags=re.DOTALL)

def split_code_logically(code_content, language):
    """Divide código em partes lógicas."""
    
    lines = code_content.split('\n')
    parts = []
    current_part = []
    
    for line in lines:
        current_part.append(line)
        
        # Dividir em pontos lógicos
        if should_split_here(line, language):
            if current_part:
                parts.append('\n'.join(current_part))
                current_part = []
    
    # Adicionar parte final
    if current_part:
        parts.append('\n'.join(current_part))
    
    return parts

def should_split_here(line, language):
    """Determina se deve dividir o código nesta linha."""
    
    stripped = line.strip()
    
    if language == 'lua':
        # Dividir após funções principais
        return (
            stripped.startswith('function ') and 
            ('init' in stripped or 'terminate' in stripped or 'on' in stripped)
        )
    elif language == 'bash':
        # Dividir após comandos principais
        return stripped.startswith('#') and 'STEP' in stripped.upper()
    else:
        return False

def add_comments_to_code_block(content, block_info, file_optimizations):
    """Adiciona comentários explicativos aos blocos de código."""
    
    pattern = r'```(\w+)?\n(.*?)```'
    
    def add_comments(match):
        language = match.group(1) or ''
        code_content = match.group(2)
        
        # Verificar se é o bloco que queremos comentar
        if not has_comments(code_content, language):
            # Adicionar comentários baseados no tipo de código
            commented_code = add_explanatory_comments(code_content, language, block_info["code_type"])
            
            file_optimizations.append({
                "type": "add_comments",
                "description": f"Adicionados comentários explicativos em {language}",
                "language": language,
                "code_type": block_info["code_type"]
            })
            
            return f"```{language}\n{commented_code}\n```"
        
        return match.group(0)
    
    return re.sub(pattern, add_comments, content, flags=re.DOTALL)

def has_comments(code_content, language):
    """Verifica se o código já tem comentários."""
    
    lines = code_content.split('\n')
    
    for line in lines:
        stripped = line.strip()
        if language == 'lua' and stripped.startswith('--'):
            return True
        elif language == 'python' and stripped.startswith('#'):
            return True
        elif language == 'javascript' and stripped.startswith('//'):
            return True
    
    return False

def add_explanatory_comments(code_content, language, code_type):
    """Adiciona comentários explicativos ao código."""
    
    lines = code_content.split('\n')
    commented_lines = []
    
    # Adicionar cabeçalho explicativo
    if language == 'lua':
        if code_type == 'module_init':
            commented_lines.append("-- ========================================")
            commented_lines.append("-- INICIALIZAÇÃO DO MÓDULO")
            commented_lines.append("-- ========================================")
            commented_lines.append("-- Esta função é chamada quando o módulo é carregado")
            commented_lines.append("-- Responsável por configurar a interface e conectar eventos")
            commented_lines.append("")
        elif code_type == 'ui_code':
            commented_lines.append("-- ========================================")
            commented_lines.append("-- CÓDIGO DE INTERFACE DO USUÁRIO")
            commented_lines.append("-- ========================================")
            commented_lines.append("-- Define a estrutura visual e comportamento da interface")
            commented_lines.append("")
        elif code_type == 'game_logic':
            commented_lines.append("-- ========================================")
            commented_lines.append("-- LÓGICA DO JOGO")
            commented_lines.append("-- ========================================")
            commented_lines.append("-- Interação com o sistema de jogo e mecânicas")
            commented_lines.append("")
    
    # Adicionar comentários em pontos específicos
    for line in lines:
        commented_lines.append(line)
        
        # Adicionar comentários explicativos em pontos importantes
        if should_add_comment_here(line, language, code_type):
            commented_lines.append(get_explanatory_comment(line, language, code_type))
    
    return '\n'.join(commented_lines)

def should_add_comment_here(line, language, code_type):
    """Determina se deve adicionar comentário nesta linha."""
    
    stripped = line.strip()
    
    if language == 'lua':
        return (
            stripped.startswith('function ') or
            stripped.startswith('local ') or
            'connect(' in stripped or
            'disconnect(' in stripped or
            'g_ui.' in stripped or
            'g_game.' in stripped
        )
    
    return False

def get_explanatory_comment(line, language, code_type):
    """Gera comentário explicativo para a linha."""
    
    stripped = line.strip()
    
    if language == 'lua':
        if stripped.startswith('function '):
            return "  -- Função principal - define o comportamento do módulo"
        elif stripped.startswith('local '):
            return "  -- Variável local - armazena dados específicos do módulo"
        elif 'connect(' in stripped:
            return "  -- Conecta evento - reage a mudanças no sistema"
        elif 'disconnect(' in stripped:
            return "  -- Desconecta evento - limpa conexões ao finalizar"
        elif 'g_ui.' in stripped:
            return "  -- Interface do usuário - cria ou modifica elementos visuais"
        elif 'g_game.' in stripped:
            return "  -- Sistema de jogo - interage com mecânicas do jogo"
    
    return "  -- Comentário explicativo"

if __name__ == "__main__":
    optimize_code_examples() 
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
- **Nome**: optimize_code_examples_processor
- **Categoria**: Scripts de Automação
- **Função**: Automação de tarefas da wiki
- **Status**: Ativo

---

