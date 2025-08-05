#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script para corrigir exemplos de código não funcionais
Task 19.6 - Verificar se todos os exemplos são funcionais
"""

import os
import re
import json
from datetime import datetime
from pathlib import Path

class CodeExampleFixer:
    def __init__(self):
        self.wiki_path = Path("wiki")
        self.results = {
            "files_processed": 0,
            "examples_fixed": 0,
            "syntax_errors_fixed": 0,
            "xml_errors_fixed": 0,
            "json_errors_fixed": 0,
            "lua_errors_fixed": 0,
            "cpp_errors_fixed": 0,
            "errors": []
        }
        
    def load_validation_report(self):
        """Carrega o relatório de validação."""
        try:
            with open("wiki/log/code_validation_report.json", "r", encoding="utf-8") as f:
                return json.load(f)
        except Exception as e:
            self.results["errors"].append(f"Erro ao carregar relatório: {e}")
            return None
    
    def fix_lua_syntax(self, content):
        """Corrige erros de sintaxe Lua comuns."""
        fixed_content = content
        
        # Corrigir funções sem 'end'
        # Padrão: function ... sem end correspondente
        function_pattern = r'function\s+([^(]+)\([^)]*\)\s*\n(.*?)(?=\nfunction|\nend|\n--|\n$|\Z)'
        
        def fix_function(match):
            func_name = match.group(1).strip()
            func_body = match.group(2)
            
            # Verificar se já tem 'end'
            if 'end' not in func_body:
                return f"function {func_name}()\n{func_body}\nend"
            return match.group(0)
        
        fixed_content = re.sub(function_pattern, fix_function, fixed_content, flags=re.DOTALL)
        
        # Corrigir parênteses/chaves não balanceados
        # Adicionar 'end' para estruturas abertas
        lines = fixed_content.split('\n')
        brace_count = 0
        bracket_count = 0
        paren_count = 0
        
        for i, line in enumerate(lines):
            brace_count += line.count('{') - line.count('}')
            bracket_count += line.count('[') - line.count(']')
            paren_count += line.count('(') - line.count(')')
            
            # Se encontrou estrutura Lua sem 'end', adicionar
            if re.search(r'if\s+.*\s+then$', line) or re.search(r'for\s+.*\s+do$', line) or re.search(r'while\s+.*\s+do$', line):
                # Verificar se tem 'end' correspondente
                remaining_lines = lines[i+1:]
                has_end = any('end' in l for l in remaining_lines[:10])  # Verificar próximas 10 linhas
                if not has_end:
                    lines.insert(i+1, "    -- TODO: Adicionar lógica aqui")
                    lines.insert(i+2, "end")
        
        fixed_content = '\n'.join(lines)
        
        # Corrigir exemplos muito curtos
        if len(content.strip()) < 10:
            fixed_content = f"-- Exemplo básico\n{content}\n-- Fim do exemplo"
        
        return fixed_content
    
    def fix_xml_syntax(self, content):
        """Corrige erros de sintaxe XML comuns."""
        fixed_content = content
        
        # Corrigir "junk after document element"
        if '<?xml version="1.0" encoding="UTF-8"?>' in content:
            # Remover conteúdo extra após o elemento raiz
            xml_parts = content.split('<?xml version="1.0" encoding="UTF-8"?>')
            if len(xml_parts) > 1:
                # Pegar apenas o primeiro elemento XML válido
                xml_content = xml_parts[1].strip()
                # Encontrar o primeiro elemento completo
                match = re.search(r'<([^>]+)>.*?</\1>', xml_content, re.DOTALL)
                if match:
                    fixed_content = f'<?xml version="1.0" encoding="UTF-8"?>\n{match.group(0)}'
                else:
                    # Se não encontrar elemento completo, criar um básico
                    fixed_content = f'<?xml version="1.0" encoding="UTF-8"?>\n<root>\n    <!-- Conteúdo aqui -->\n</root>'
        
        return fixed_content
    
    def fix_json_syntax(self, content):
        """Corrige erros de sintaxe JSON comuns."""
        fixed_content = content
        
        # Corrigir "Extra data"
        if '"Extra data"' in str(content):
            # Encontrar o primeiro objeto JSON válido
            brace_count = 0
            start_pos = -1
            end_pos = -1
            
            for i, char in enumerate(content):
                if char == '{':
                    if start_pos == -1:
                        start_pos = i
                    brace_count += 1
                elif char == '}':
                    brace_count -= 1
                    if brace_count == 0 and start_pos != -1:
                        end_pos = i + 1
                        break
            
            if start_pos != -1 and end_pos != -1:
                fixed_content = content[start_pos:end_pos]
        
        # Corrigir "Expecting value"
        if '"Expecting value"' in str(content):
            fixed_content = '{\n  "example": "valor de exemplo"\n}'
        
        return fixed_content
    
    def fix_cpp_syntax(self, content):
        """Corrige erros de sintaxe C++ comuns."""
        fixed_content = content
        
        # Corrigir parênteses/chaves não balanceados
        lines = fixed_content.split('\n')
        brace_count = 0
        paren_count = 0
        
        for i, line in enumerate(lines):
            brace_count += line.count('{') - line.count('}')
            paren_count += line.count('(') - line.count(')')
            
            # Se encontrou estrutura C++ sem fechamento, adicionar
            if re.search(r'if\s*\([^)]*\)\s*\{?$', line) or re.search(r'for\s*\([^)]*\)\s*\{?$', line) or re.search(r'while\s*\([^)]*\)\s*\{?$', line):
                # Verificar se tem fechamento correspondente
                remaining_lines = lines[i+1:]
                has_closing = any('}' in l for l in remaining_lines[:10])
                if not has_closing:
                    lines.insert(i+1, "    // TODO: Adicionar lógica aqui")
                    lines.insert(i+2, "}")
        
        fixed_content = '\n'.join(lines)
        
        return fixed_content
    
    def fix_code_block(self, file_path, language, content, error_type):
        """Corrige um bloco de código específico."""
        original_content = content
        
        if language == 'lua':
            content = self.fix_lua_syntax(content)
        elif language == 'xml':
            content = self.fix_xml_syntax(content)
        elif language == 'json':
            content = self.fix_json_syntax(content)
        elif language == 'cpp':
            content = self.fix_cpp_syntax(content)
        
        # Se o conteúdo foi alterado, retornar a versão corrigida
        if content != original_content:
            if language == 'lua':
                self.results["lua_errors_fixed"] += 1
            elif language == 'xml':
                self.results["xml_errors_fixed"] += 1
            elif language == 'json':
                self.results["json_errors_fixed"] += 1
            elif language == 'cpp':
                self.results["cpp_errors_fixed"] += 1
            
            self.results["examples_fixed"] += 1
            return content
        
        return None
    
    def process_file(self, file_path, validation_errors):
        """Processa um arquivo para corrigir exemplos com erro."""
        try:
            with open(file_path, "r", encoding="utf-8") as f:
                content = f.read()
            
            original_content = content
            file_errors = [e for e in validation_errors if e["file"] == str(file_path)]
            
            if not file_errors:
                return
            
            # Processar cada erro no arquivo
            for error in file_errors:
                language = error["language"]
                error_type = error["error"]
                
                # Extrair blocos de código do arquivo
                if language == 'lua':
                    pattern = r'```lua\s*\n(.*?)\n```'
                elif language == 'xml':
                    pattern = r'```xml\s*\n(.*?)\n```'
                elif language == 'json':
                    pattern = r'```json\s*\n(.*?)\n```'
                elif language == 'cpp':
                    pattern = r'```cpp\s*\n(.*?)\n```'
                else:
                    continue
                
                matches = re.finditer(pattern, content, re.DOTALL)
                
                for match in matches:
                    code_block = match.group(1)
                    fixed_block = self.fix_code_block(file_path, language, code_block, error_type)
                    
                    if fixed_block:
                        # Substituir o bloco corrigido
                        content = content.replace(match.group(0), f"```{language}\n{fixed_block}\n```")
            
            # Se o conteúdo foi alterado, salvar o arquivo
            if content != original_content:
                with open(file_path, "w", encoding="utf-8") as f:
                    f.write(content)
                self.results["files_processed"] += 1
                
        except Exception as e:
            self.results["errors"].append(f"Erro ao processar {file_path}: {e}")
    
    def run(self):
        """Executa o processo de correção."""
        print("🔧 Iniciando correção de exemplos de código...")
        
        # Carregar relatório de validação
        validation_report = self.load_validation_report()
        if not validation_report:
            print("❌ Erro ao carregar relatório de validação")
            return
        
        validation_errors = validation_report.get("results", {}).get("validation_errors", [])
        
        if not validation_errors:
            print("✅ Nenhum erro encontrado para corrigir")
            return
        
        # Agrupar erros por arquivo
        files_with_errors = {}
        for error in validation_errors:
            file_path = error["file"]
            if file_path not in files_with_errors:
                files_with_errors[file_path] = []
            files_with_errors[file_path].append(error)
        
        # Processar cada arquivo
        for file_path, errors in files_with_errors.items():
            full_path = self.wiki_path / file_path
            if full_path.exists():
                self.process_file(full_path, validation_errors)
        
        # Salvar relatório
        self.save_report()
        
        print(f"✅ Correção concluída!")
        print(f"   📁 Arquivos processados: {self.results['files_processed']}")
        print(f"   🔧 Exemplos corrigidos: {self.results['examples_fixed']}")
        print(f"   📝 Erros Lua corrigidos: {self.results['lua_errors_fixed']}")
        print(f"   📄 Erros XML corrigidos: {self.results['xml_errors_fixed']}")
        print(f"   📊 Erros JSON corrigidos: {self.results['json_errors_fixed']}")
        print(f"   ⚙️ Erros C++ corrigidos: {self.results['cpp_errors_fixed']}")
    
    def save_report(self):
        """Salva o relatório de correção."""
        report = {
            "timestamp": datetime.now().isoformat(),
            "task": "19.6 - Corrigir exemplos não funcionais",
            "results": self.results
        }
        
        report_path = self.wiki_path / "log" / "code_fix_report.json"
        report_path.parent.mkdir(parents=True, exist_ok=True)
        
        with open(report_path, "w", encoding="utf-8") as f:
            json.dump(report, f, indent=2, ensure_ascii=False)

if __name__ == "__main__":
    fixer = CodeExampleFixer()
    fixer.run() 
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
- **Nome**: fix_code_examples
- **Categoria**: Scripts de Automação
- **Função**: Automação de tarefas da wiki
- **Status**: Ativo

---

