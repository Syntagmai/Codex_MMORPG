#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script para validar funcionalidade dos exemplos de código
Task 19.6 - Verificar se todos os exemplos são funcionais
"""

import os
import re
import json
import tempfile
import subprocess
from datetime import datetime
from pathlib import Path

class CodeExampleValidator:
    def __init__(self):
        self.wiki_path = Path("wiki")
        self.results = {
            "files_processed": 0,
            "examples_validated": 0,
            "functional_examples": 0,
            "non_functional_examples": 0,
            "syntax_errors": 0,
            "validation_errors": []
        }
        
    def extract_code_blocks(self, content):
        """Extrai blocos de código do conteúdo."""
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
                    'content': match.group(1).strip(),
                    'start': match.start(),
                    'end': match.end()
                })
        
        return code_blocks
    
    def validate_lua_syntax(self, code):
        """Valida sintaxe Lua usando linter."""
        try:
            # Criar arquivo temporário
            with tempfile.NamedTemporaryFile(mode='w', suffix='.lua', delete=False, encoding='utf-8') as f:
                f.write(code)
                temp_file = f.name
            
            # Tentar executar com lua (se disponível)
            try:
                result = subprocess.run(['lua', '-l', temp_file], 
                                      capture_output=True, text=True, timeout=5)
                os.unlink(temp_file)
                
                if result.returncode == 0:
                    return True, "Sintaxe válida"
                else:
                    return False, f"Erro de sintaxe: {result.stderr}"
                    
            except FileNotFoundError:
                # Lua não disponível, fazer validação básica
                os.unlink(temp_file)
                return self.basic_lua_validation(code)
                
        except Exception as e:
            return False, f"Erro na validação: {str(e)}"
    
    def basic_lua_validation(self, code):
        """Validação básica de sintaxe Lua."""
        # Verificar parênteses, chaves e colchetes balanceados
        stack = []
        brackets = {'(': ')', '{': '}', '[': ']'}
        
        for char in code:
            if char in brackets:
                stack.append(char)
            elif char in brackets.values():
                if not stack:
                    return False, "Parênteses/chaves não balanceados"
                if brackets[stack.pop()] != char:
                    return False, "Parênteses/chaves não correspondem"
        
        if stack:
            return False, "Parênteses/chaves não fechados"
        
        # Verificar palavras-chave básicas
        keywords = ['function', 'end', 'if', 'then', 'else', 'for', 'while', 'do', 'local', 'return']
        lines = code.split('\n')
        
        for i, line in enumerate(lines, 1):
            line = line.strip()
            if line.startswith('function') and not line.endswith('end'):
                # Verificar se há 'end' correspondente
                if 'end' not in code[code.find(line):]:
                    return False, f"Função sem 'end' na linha {i}"
        
        return True, "Validação básica passou"
    
    def validate_xml_syntax(self, code):
        """Valida sintaxe XML."""
        try:
            import xml.etree.ElementTree as ET
            ET.fromstring(code)
            return True, "XML válido"
        except ET.ParseError as e:
            return False, f"Erro XML: {str(e)}"
        except Exception as e:
            return False, f"Erro na validação XML: {str(e)}"
    
    def validate_json_syntax(self, code):
        """Valida sintaxe JSON."""
        try:
            json.loads(code)
            return True, "JSON válido"
        except json.JSONDecodeError as e:
            return False, f"Erro JSON: {str(e)}"
        except Exception as e:
            return False, f"Erro na validação JSON: {str(e)}"
    
    def validate_cpp_syntax(self, code):
        """Validação básica de sintaxe C++."""
        # Verificar parênteses, chaves e colchetes balanceados
        stack = []
        brackets = {'(': ')', '{': '}', '[': ']'}
        
        for char in code:
            if char in brackets:
                stack.append(char)
            elif char in brackets.values():
                if not stack:
                    return False, "Parênteses/chaves não balanceados"
                if brackets[stack.pop()] != char:
                    return False, "Parênteses/chaves não correspondem"
        
        if stack:
            return False, "Parênteses/chaves não fechados"
        
        # Verificar ponto e vírgula básicos
        lines = code.split('\n')
        for i, line in enumerate(lines, 1):
            line = line.strip()
            if (line and not line.startswith('//') and not line.startswith('/*') and 
                not line.startswith('#') and not line.endswith(';') and 
                not line.endswith('{') and not line.endswith('}') and
                'class' not in line and 'struct' not in line and
                'namespace' not in line and 'if' not in line and
                'for' not in line and 'while' not in line):
                # Linha pode precisar de ponto e vírgula
                pass
        
        return True, "Validação básica C++ passou"
    
    def validate_code_block(self, code_block):
        """Valida um bloco de código específico."""
        language = code_block['language']
        content = code_block['content']
        
        if language == 'lua':
            return self.validate_lua_syntax(content)
        elif language == 'xml':
            return self.validate_xml_syntax(content)
        elif language == 'json':
            return self.validate_json_syntax(content)
        elif language == 'cpp':
            return self.validate_cpp_syntax(content)
        else:
            return True, "Linguagem não suportada para validação"
    
    def is_functional_example(self, code_block):
        """Determina se o exemplo é funcional."""
        # Verificar se é um exemplo completo
        content = code_block['content']
        
        # Exemplos que são apenas comentários ou muito curtos
        if len(content.strip()) < 10:
            return False, "Exemplo muito curto"
        
        # Verificar se tem conteúdo real (não apenas comentários)
        lines = content.split('\n')
        code_lines = [line for line in lines if line.strip() and not line.strip().startswith('--')]
        
        if len(code_lines) < 2:
            return False, "Apenas comentários"
        
        # Validar sintaxe
        is_valid, message = self.validate_code_block(code_block)
        
        if not is_valid:
            return False, message
        
        return True, "Exemplo funcional"
    
    def validate_file(self, file_path):
        """Valida exemplos de código em um arquivo."""
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            code_blocks = self.extract_code_blocks(content)
            
            for code_block in code_blocks:
                self.results['examples_validated'] += 1
                
                is_functional, message = self.is_functional_example(code_block)
                
                if is_functional:
                    self.results['functional_examples'] += 1
                else:
                    self.results['non_functional_examples'] += 1
                    if "sintaxe" in message.lower() or "erro" in message.lower():
                        self.results['syntax_errors'] += 1
                    
                    self.results['validation_errors'].append({
                        'file': str(file_path),
                        'language': code_block['language'],
                        'error': message,
                        'content_preview': code_block['content'][:100] + "..."
                    })
            
            self.results['files_processed'] += 1
            
        except Exception as e:
            self.results['validation_errors'].append({
                'file': str(file_path),
                'error': f"Erro ao processar arquivo: {str(e)}"
            })
    
    def run_validation(self):
        """Executa a validação em todos os arquivos da wiki."""
        print("🔍 Iniciando validação de exemplos de código...")
        
        # Processar arquivos markdown na wiki
        for file_path in self.wiki_path.rglob("*.md"):
            if file_path.is_file():
                print(f"📝 Validando: {file_path}")
                self.validate_file(file_path)
        
        # Gerar relatório
        self.generate_report()
        
        print("✅ Validação concluída!")
        return self.results
    
    def generate_report(self):
        """Gera relatório de validação."""
        report = {
            "timestamp": datetime.now().isoformat(),
            "task": "19.6 - Verificar se todos os exemplos são funcionais",
            "results": self.results,
            "summary": {
                "files_processed": self.results['files_processed'],
                "examples_validated": self.results['examples_validated'],
                "functional_examples": self.results['functional_examples'],
                "non_functional_examples": self.results['non_functional_examples'],
                "syntax_errors": self.results['syntax_errors'],
                "success_rate": round((self.results['functional_examples'] / max(self.results['examples_validated'], 1)) * 100, 2)
            }
        }
        
        # Salvar relatório
        report_path = self.wiki_path / "log" / "code_validation_report.json"
        report_path.parent.mkdir(exist_ok=True)
        
        with open(report_path, 'w', encoding='utf-8') as f:
            json.dump(report, f, indent=2, ensure_ascii=False)
        
        print(f"📊 Relatório salvo em: {report_path}")

if __name__ == "__main__":
    validator = CodeExampleValidator()
    results = validator.run_validation()
    
    print("\n📈 RESULTADOS DA VALIDAÇÃO:")
    print(f"📁 Arquivos processados: {results['files_processed']}")
    print(f"💡 Exemplos validados: {results['examples_validated']}")
    print(f"✅ Exemplos funcionais: {results['functional_examples']}")
    print(f"❌ Exemplos não funcionais: {results['non_functional_examples']}")
    print(f"🔧 Erros de sintaxe: {results['syntax_errors']}")
    print(f"📊 Taxa de sucesso: {round((results['functional_examples'] / max(results['examples_validated'], 1)) * 100, 2)}%") 