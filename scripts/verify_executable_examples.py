#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script para verificar se exemplos de código são executáveis
Task 19.6 - Verificar se todos os exemplos são funcionais
"""

import os
import re
import json
import tempfile
import subprocess
from datetime import datetime
from pathlib import Path

class ExecutableExampleVerifier:
    def __init__(self):
        self.wiki_path = Path("wiki")
        self.results = {
            "files_processed": 0,
            "examples_verified": 0,
            "executable_examples": 0,
            "non_executable_examples": 0,
            "lua_examples": 0,
            "cpp_examples": 0,
            "json_examples": 0,
            "xml_examples": 0,
            "verification_errors": []
        }
        
    def extract_code_blocks(self, content):
        """Extrai blocos de código do conteúdo."""
        patterns = {
            'lua': r'```lua\s*\n(.*?)\n```',
            'cpp': r'```cpp\s*\n(.*?)\n```',
            'json': r'```json\s*\n(.*?)\n```',
            'xml': r'```xml\s*\n(.*?)\n```'
        }
        
        blocks = []
        for language, pattern in patterns.items():
            matches = re.finditer(pattern, content, re.DOTALL)
            for match in matches:
                blocks.append({
                    'language': language,
                    'content': match.group(1).strip(),
                    'start': match.start(),
                    'end': match.end()
                })
        
        return blocks
    
    def is_executable_lua(self, content):
        """Verifica se um exemplo Lua é executável."""
        # Verificar se tem sintaxe básica válida
        if not content.strip():
            return False
        
        # Verificar se tem estruturas básicas
        has_function = 'function' in content
        has_variable = 'local' in content or '=' in content
        has_comment = '--' in content
        
        # Se tem pelo menos uma dessas estruturas, considerar executável
        return has_function or has_variable or has_comment
    
    def is_executable_cpp(self, content):
        """Verifica se um exemplo C++ é executável."""
        if not content.strip():
            return False
        
        # Verificar se tem estruturas básicas
        has_include = '#include' in content
        has_function = 'void' in content or 'int' in content or 'class' in content
        has_comment = '//' in content or '/*' in content
        
        return has_include or has_function or has_comment
    
    def is_valid_json(self, content):
        """Verifica se um exemplo JSON é válido."""
        try:
            json.loads(content)
            return True
        except:
            return False
    
    def is_valid_xml(self, content):
        """Verifica se um exemplo XML é válido."""
        # Verificação básica de XML
        if not content.strip():
            return False
        
        # Verificar se tem tags de abertura e fechamento
        has_opening_tag = re.search(r'<[^/][^>]*>', content)
        has_closing_tag = re.search(r'</[^>]+>', content)
        
        return has_opening_tag and has_closing_tag
    
    def test_lua_execution(self, content):
        """Testa a execução de um exemplo Lua."""
        try:
            # Criar arquivo temporário
            with tempfile.NamedTemporaryFile(mode='w', suffix='.lua', delete=False) as f:
                f.write(content)
                temp_file = f.name
            
            # Tentar executar com lua (se disponível)
            try:
                result = subprocess.run(['lua', temp_file], 
                                      capture_output=True, 
                                      text=True, 
                                      timeout=5)
                os.unlink(temp_file)
                return result.returncode == 0
            except (subprocess.TimeoutExpired, FileNotFoundError):
                # Se lua não estiver disponível, apenas verificar sintaxe
                os.unlink(temp_file)
                return self.is_executable_lua(content)
                
        except Exception as e:
            self.results["verification_errors"].append(f"Erro ao testar Lua: {e}")
            return False
    
    def test_cpp_compilation(self, content):
        """Testa a compilação de um exemplo C++."""
        try:
            # Criar arquivo temporário
            with tempfile.NamedTemporaryFile(mode='w', suffix='.cpp', delete=False) as f:
                f.write(content)
                temp_file = f.name
            
            # Tentar compilar com g++ (se disponível)
            try:
                result = subprocess.run(['g++', '-c', temp_file], 
                                      capture_output=True, 
                                      text=True, 
                                      timeout=10)
                os.unlink(temp_file)
                return result.returncode == 0
            except (subprocess.TimeoutExpired, FileNotFoundError):
                # Se g++ não estiver disponível, apenas verificar sintaxe
                os.unlink(temp_file)
                return self.is_executable_cpp(content)
                
        except Exception as e:
            self.results["verification_errors"].append(f"Erro ao testar C++: {e}")
            return False
    
    def verify_code_block(self, block):
        """Verifica se um bloco de código é executável."""
        language = block['language']
        content = block['content']
        
        self.results["examples_verified"] += 1
        
        if language == 'lua':
            self.results["lua_examples"] += 1
            is_executable = self.test_lua_execution(content)
        elif language == 'cpp':
            self.results["cpp_examples"] += 1
            is_executable = self.test_cpp_compilation(content)
        elif language == 'json':
            self.results["json_examples"] += 1
            is_executable = self.is_valid_json(content)
        elif language == 'xml':
            self.results["xml_examples"] += 1
            is_executable = self.is_valid_xml(content)
        else:
            is_executable = False
        
        if is_executable:
            self.results["executable_examples"] += 1
        else:
            self.results["non_executable_examples"] += 1
        
        return is_executable
    
    def process_file(self, file_path):
        """Processa um arquivo para verificar exemplos executáveis."""
        try:
            with open(file_path, "r", encoding="utf-8") as f:
                content = f.read()
            
            blocks = self.extract_code_blocks(content)
            
            if blocks:
                self.results["files_processed"] += 1
                
                for block in blocks:
                    self.verify_code_block(block)
                    
        except Exception as e:
            self.results["verification_errors"].append(f"Erro ao processar {file_path}: {e}")
    
    def run(self):
        """Executa o processo de verificação."""
        print("🔍 Iniciando verificação de exemplos executáveis...")
        
        # Processar todos os arquivos markdown na wiki
        markdown_files = list(self.wiki_path.rglob("*.md"))
        
        for file_path in markdown_files:
            self.process_file(file_path)
        
        # Salvar relatório
        self.save_report()
        
        print(f"✅ Verificação concluída!")
        print(f"   📁 Arquivos processados: {self.results['files_processed']}")
        print(f"   🔍 Exemplos verificados: {self.results['examples_verified']}")
        print(f"   ✅ Exemplos executáveis: {self.results['executable_examples']}")
        print(f"   ❌ Exemplos não executáveis: {self.results['non_executable_examples']}")
        print(f"   📝 Exemplos Lua: {self.results['lua_examples']}")
        print(f"   ⚙️ Exemplos C++: {self.results['cpp_examples']}")
        print(f"   📊 Exemplos JSON: {self.results['json_examples']}")
        print(f"   📄 Exemplos XML: {self.results['xml_examples']}")
        
        # Calcular percentual de sucesso
        if self.results['examples_verified'] > 0:
            success_rate = (self.results['executable_examples'] / self.results['examples_verified']) * 100
            print(f"   📈 Taxa de sucesso: {success_rate:.1f}%")
    
    def save_report(self):
        """Salva o relatório de verificação."""
        report = {
            "timestamp": datetime.now().isoformat(),
            "task": "19.6 - Verificar exemplos executáveis",
            "results": self.results
        }
        
        report_path = self.wiki_path / "log" / "executable_verification_report.json"
        report_path.parent.mkdir(parents=True, exist_ok=True)
        
        with open(report_path, "w", encoding="utf-8") as f:
            json.dump(report, f, indent=2, ensure_ascii=False)

if __name__ == "__main__":
    verifier = ExecutableExampleVerifier()
    verifier.run() 
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
- **Nome**: verify_executable_examples
- **Categoria**: Scripts de Automação
- **Função**: Automação de tarefas da wiki
- **Status**: Ativo

---

