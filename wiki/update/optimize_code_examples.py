#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script para otimizar exemplos de código na wiki
Task 19.6 - Otimizar Exemplos e Código
"""

import os
import re
import json
from datetime import datetime
from pathlib import Path

class CodeExampleOptimizer:
    def __init__(self):
        self.wiki_path = Path("wiki")
        self.results = {
            "files_processed": 0,
            "examples_optimized": 0,
            "long_examples_divided": 0,
            "comments_added": 0,
            "errors": []
        }
        
    def analyze_code_blocks(self, content):
        """Analisa blocos de código no conteúdo."""
        # Padrões para diferentes tipos de código
        patterns = {
            'lua': r'```lua\s*\n(.*?)\n```',
            'cpp': r'```cpp\s*\n(.*?)\n```',
            'xml': r'```xml\s*\n(.*?)\n```',
            'json': r'```json\s*\n(.*?)\n```'
        }
        
        code_blocks = []
        for lang, pattern in patterns.items():
            matches = re.finditer(pattern, content, re.DOTALL)
            for match in matches:
                code_blocks.append({
                    'language': lang,
                    'content': match.group(1),
                    'start': match.start(),
                    'end': match.end(),
                    'full_match': match.group(0)
                })
        
        return code_blocks
    
    def is_long_example(self, code_block):
        """Verifica se o exemplo é muito longo (>50 linhas)."""
        lines = code_block['content'].split('\n')
        return len(lines) > 50
    
    def needs_comments(self, code_block):
        """Verifica se o código precisa de comentários em português."""
        content = code_block['content'].lower()
        # Verifica se já tem comentários em português
        portuguese_comments = re.findall(r'--.*[àáâãäåæçèéêëìíîïðñòóôõöøùúûüýþÿ]', content)
        return len(portuguese_comments) < 3  # Menos de 3 comentários em português
    
    def divide_long_example(self, code_block):
        """Divide exemplos longos em partes menores."""
        lines = code_block['content'].split('\n')
        divided_parts = []
        
        # Identificar seções lógicas
        sections = []
        current_section = []
        
        for line in lines:
            current_section.append(line)
            
            # Detectar fim de seção (função, classe, etc.)
            if (line.strip().startswith('end') or 
                line.strip().startswith('}') or
                line.strip().startswith('};') or
                re.match(r'^\s*function\s+', line.strip()) or
                re.match(r'^\s*class\s+', line.strip())):
                
                if len(current_section) > 20:  # Seção muito longa
                    sections.append(current_section)
                    current_section = []
        
        if current_section:
            sections.append(current_section)
        
        # Criar partes divididas
        for i, section in enumerate(sections):
            section_title = f"Parte {i+1}"
            if i == 0:
                section_title = "Inicialização e Configuração"
            elif i == len(sections) - 1:
                section_title = "Finalização"
            else:
                section_title = f"Funcionalidade {i}"
            
            divided_parts.append({
                'title': section_title,
                'content': '\n'.join(section),
                'language': code_block['language']
            })
        
        return divided_parts
    
    def add_portuguese_comments(self, code_block):
        """Adiciona comentários explicativos em português."""
        content = code_block['content']
        lines = content.split('\n')
        commented_lines = []
        
        for i, line in enumerate(lines):
            commented_lines.append(line)
            
            # Adicionar comentários explicativos
            if re.match(r'^\s*function\s+', line.strip()):
                func_name = re.search(r'function\s+(\w+)', line.strip())
                if func_name:
                    commented_lines.append(f"    -- Função: {func_name.group(1)}")
            
            elif re.match(r'^\s*class\s+', line.strip()):
                class_name = re.search(r'class\s+(\w+)', line.strip())
                if class_name:
                    commented_lines.append(f"    -- Classe: {class_name.group(1)}")
            
            elif re.match(r'^\s*if\s+', line.strip()) and 'then' in line:
                commented_lines.append("    -- Verificação condicional")
            
            elif re.match(r'^\s*for\s+', line.strip()) and 'do' in line:
                commented_lines.append("    -- Loop de repetição")
            
            elif re.match(r'^\s*while\s+', line.strip()) and 'do' in line:
                commented_lines.append("    -- Loop condicional")
            
            elif line.strip().startswith('--') and not any(char in line for char in 'àáâãäåæçèéêëìíîïðñòóôõöøùúûüýþÿ'):
                # Comentário em inglês, adicionar tradução
                commented_lines.append(f"    -- {line.strip()[2:]} (traduzido)")
        
        return '\n'.join(commented_lines)
    
    def create_progressive_example(self, code_block):
        """Cria exemplo progressivo (básico → avançado)."""
        content = code_block['content']
        
        # Identificar nível de complexidade
        complexity_indicators = {
            'basic': ['print', 'local', 'function', 'if', 'then', 'end'],
            'intermediate': ['for', 'while', 'table', 'pairs', 'ipairs'],
            'advanced': ['coroutine', 'metatable', 'pcall', 'xpcall', 'require']
        }
        
        level = 'basic'
        for indicator in complexity_indicators['advanced']:
            if indicator in content:
                level = 'advanced'
                break
        else:
            for indicator in complexity_indicators['intermediate']:
                if indicator in content:
                    level = 'intermediate'
                    break
        
        # Criar versão progressiva
        if level == 'basic':
            return {
                'basic': content,
                'intermediate': self.add_intermediate_features(content),
                'advanced': self.add_advanced_features(content)
            }
        elif level == 'intermediate':
            return {
                'basic': self.extract_basic_part(content),
                'intermediate': content,
                'advanced': self.add_advanced_features(content)
            }
        else:  # advanced
            return {
                'basic': self.extract_basic_part(content),
                'intermediate': self.extract_intermediate_part(content),
                'advanced': content
            }
    
    def add_intermediate_features(self, basic_code):
        """Adiciona recursos intermediários ao código básico."""
        features = [
            "\n-- Adicionar tratamento de erros",
            "local success, result = pcall(function()",
            "    -- Código original aqui",
            "end)",
            "if not success then",
            "    print('Erro:', result)",
            "end"
        ]
        return basic_code + '\n'.join(features)
    
    def add_advanced_features(self, intermediate_code):
        """Adiciona recursos avançados ao código intermediário."""
        features = [
            "\n-- Adicionar metatable para funcionalidade avançada",
            "local mt = {",
            "    __index = function(t, k)",
            "        return rawget(t, k) or 'Valor não encontrado'",
            "    end",
            "    __call = function(t, ...)",
            "        print('Objeto chamado com:', ...)",
            "    end",
            "}",
            "setmetatable(meuObjeto, mt)"
        ]
        return intermediate_code + '\n'.join(features)
    
    def extract_basic_part(self, advanced_code):
        """Extrai parte básica do código avançado."""
        lines = advanced_code.split('\n')
        basic_lines = []
        
        for line in lines:
            # Incluir apenas linhas básicas
            if any(indicator in line for indicator in ['print', 'local', 'function', 'if', 'then', 'end']):
                basic_lines.append(line)
            elif line.strip().startswith('--'):
                basic_lines.append(line)
        
        return '\n'.join(basic_lines)
    
    def extract_intermediate_part(self, advanced_code):
        """Extrai parte intermediária do código avançado."""
        lines = advanced_code.split('\n')
        intermediate_lines = []
        
        for line in lines:
            # Excluir linhas muito avançadas
            if not any(advanced in line for advanced in ['coroutine', 'metatable', 'pcall', 'xpcall']):
                intermediate_lines.append(line)
        
        return '\n'.join(intermediate_lines)
    
    def optimize_file(self, file_path):
        """Otimiza exemplos de código em um arquivo."""
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            original_content = content
            code_blocks = self.analyze_code_blocks(content)
            
            for code_block in code_blocks:
                optimized = False
                
                # Dividir exemplos longos
                if self.is_long_example(code_block):
                    divided_parts = self.divide_long_example(code_block)
                    if len(divided_parts) > 1:
                        # Substituir exemplo longo por versões divididas
                        replacement = "\n\n".join([
                            f"#### {part['title']}\n```{part['language']}\n{part['content']}\n```"
                            for part in divided_parts
                        ])
                        content = content.replace(code_block['full_match'], replacement)
                        self.results['long_examples_divided'] += 1
                        optimized = True
                
                # Adicionar comentários em português
                if self.needs_comments(code_block):
                    commented_content = self.add_portuguese_comments(code_block)
                    new_block = f"```{code_block['language']}\n{commented_content}\n```"
                    content = content.replace(code_block['full_match'], new_block)
                    self.results['comments_added'] += 1
                    optimized = True
                
                # Criar exemplo progressivo
                progressive_example = self.create_progressive_example(code_block)
                if len(progressive_example) > 1:
                    # Substituir por versão progressiva
                    replacement = "\n\n".join([
                        f"#### Nível {level.title()}\n```{code_block['language']}\n{prog_content}\n```"
                        for level, prog_content in progressive_example.items()
                    ])
                    content = content.replace(code_block['full_match'], replacement)
                    optimized = True
                
                if optimized:
                    self.results['examples_optimized'] += 1
            
            # Salvar arquivo otimizado
            if content != original_content:
                with open(file_path, 'w', encoding='utf-8') as f:
                    f.write(content)
            
            self.results['files_processed'] += 1
            
        except Exception as e:
            self.results['errors'].append(f"Erro em {file_path}: {str(e)}")
    
    def run_optimization(self):
        """Executa a otimização em todos os arquivos da wiki."""
        print("🔧 Iniciando otimização de exemplos de código...")
        
        # Processar arquivos markdown na wiki
        for file_path in self.wiki_path.rglob("*.md"):
            if file_path.is_file():
                print(f"📝 Processando: {file_path}")
                self.optimize_file(file_path)
        
        # Gerar relatório
        self.generate_report()
        
        print("✅ Otimização concluída!")
        return self.results
    
    def generate_report(self):
        """Gera relatório de otimização."""
        report = {
            "timestamp": datetime.now().isoformat(),
            "task": "19.6 - Otimizar Exemplos e Código",
            "results": self.results,
            "summary": {
                "files_processed": self.results['files_processed'],
                "examples_optimized": self.results['examples_optimized'],
                "long_examples_divided": self.results['long_examples_divided'],
                "comments_added": self.results['comments_added'],
                "errors_count": len(self.results['errors'])
            }
        }
        
        # Salvar relatório
        report_path = self.wiki_path / "log" / "code_optimization_report.json"
        report_path.parent.mkdir(exist_ok=True)
        
        with open(report_path, 'w', encoding='utf-8') as f:
            json.dump(report, f, indent=2, ensure_ascii=False)
        
        print(f"📊 Relatório salvo em: {report_path}")

if __name__ == "__main__":
    optimizer = CodeExampleOptimizer()
    results = optimizer.run_optimization()
    
    print("\n📈 RESULTADOS DA OTIMIZAÇÃO:")
    print(f"📁 Arquivos processados: {results['files_processed']}")
    print(f"💡 Exemplos otimizados: {results['examples_optimized']}")
    print(f"✂️ Exemplos longos divididos: {results['long_examples_divided']}")
    print(f"💬 Comentários adicionados: {results['comments_added']}")
    print(f"❌ Erros: {len(results['errors'])}") 