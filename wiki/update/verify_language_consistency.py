#!/usr/bin/env python3
"""
Script para verificar consistência de idioma em toda a documentação da wiki.
Verifica se os termos técnicos estão padronizados em português brasileiro.
"""

import os
import re
import json
from datetime import datetime
from pathlib import Path

class LanguageConsistencyChecker:
    def __init__(self):
        self.wiki_path = Path("wiki")
        self.report_path = Path("wiki/maps/language_consistency_report.json")
        
        # Termos técnicos que devem estar em português
        self.technical_terms = {
            # Programação geral
            "function": "função",
            "class": "classe", 
            "method": "método",
            "variable": "variável",
            "parameter": "parâmetro",
            "return": "retornar",
            "import": "importar",
            "export": "exportar",
            "module": "módulo",
            "interface": "interface",
            "type": "tipo",
            "enum": "enumeração",
            "struct": "estrutura",
            "namespace": "espaço de nomes",
            "template": "modelo",
            "macro": "macro",
            "callback": "função de retorno",
            "event": "evento",
            "signal": "sinal",
            "slot": "conector",
            "property": "propriedade",
            "attribute": "atributo",
            "field": "campo",
            "member": "membro",
            "constructor": "construtor",
            "destructor": "destruidor",
            "inheritance": "herança",
            "polymorphism": "polimorfismo",
            "encapsulation": "encapsulamento",
            "abstraction": "abstração",
            "overload": "sobrecarga",
            "override": "sobrescrever",
            "virtual": "virtual",
            "static": "estático",
            "const": "constante",
            "volatile": "volátil",
            "mutable": "mutável",
            "explicit": "explícito",
            "implicit": "implícito",
            "inline": "em linha",
            "extern": "externo",
            "register": "registrador",
            "auto": "automático",
            "decltype": "tipo declarado",
            "nullptr": "ponteiro nulo",
            "constexpr": "constante de compilação",
            "noexcept": "sem exceção",
            "final": "final",
            "delete": "excluir",
            "default": "padrão",
            "public": "público",
            "private": "privado",
            "protected": "protegido",
            "friend": "amigo",
            "pure": "puro",
            "abstract": "abstrato",
            "sealed": "selado",
            "delegate": "delegado",
            "indexer": "indexador",
            "operator": "operador",
            "conversion": "conversão",
            "cast": "conversão explícita",
            "typeid": "identificador de tipo",
            "sizeof": "tamanho de",
            "alignof": "alinhamento de",
            "offsetof": "deslocamento de",
            
            # Desenvolvimento de jogos
            "game engine": "motor de jogo",
            "renderer": "renderizador",
            "sprite": "sprite",
            "texture": "textura",
            "mesh": "malha",
            "shader": "shader",
            "animation": "animação",
            "physics": "física",
            "collision": "colisão",
            "input": "entrada",
            "output": "saída",
            "update": "atualizar",
            "draw": "desenhar",
            "load": "carregar",
            "save": "salvar",
            "spawn": "gerar",
            "destroy": "destruir",
            "instantiate": "instanciar",
            "prefab": "prefabricado",
            "component": "componente",
            "system": "sistema",
            "entity": "entidade",
            "scene": "cena",
            "level": "nível",
            "stage": "estágio",
            "checkpoint": "ponto de verificação",
            "savepoint": "ponto de salvamento",
            "respawn": "renascimento",
            "respawn point": "ponto de renascimento",
            
            # Interface/Web
            "widget": "widget",
            "button": "botão",
            "textbox": "caixa de texto",
            "label": "rótulo",
            "panel": "painel",
            "window": "janela",
            "dialog": "diálogo",
            "modal": "modal",
            "popup": "popup",
            "menu": "menu",
            "toolbar": "barra de ferramentas",
            "statusbar": "barra de status",
            "scrollbar": "barra de rolagem",
            "tab": "aba",
            "list": "lista",
            "tree": "árvore",
            "grid": "grade",
            "table": "tabela",
            "form": "formulário",
            "field": "campo",
            "input": "entrada",
            "output": "saída",
            "submit": "enviar",
            "reset": "redefinir",
            "validate": "validar",
            "error": "erro",
            "warning": "aviso",
            "info": "informação",
            "success": "sucesso",
            
            # Sistema e arquivos
            "file": "arquivo",
            "folder": "pasta",
            "directory": "diretório",
            "path": "caminho",
            "filename": "nome do arquivo",
            "extension": "extensão",
            "format": "formato",
            "encoding": "codificação",
            "binary": "binário",
            "text": "texto",
            "config": "configuração",
            "settings": "configurações",
            "log": "log",
            "error log": "log de erros",
            "debug": "depuração",
            "debugger": "depurador",
            "profiler": "analisador",
            "compiler": "compilador",
            "interpreter": "interpretador",
            "runtime": "tempo de execução",
            "build": "compilação",
            "deploy": "implantação",
            "release": "lançamento",
            "version": "versão",
            "patch": "correção",
            "update": "atualização"
        }
        
        # Termos que devem permanecer em inglês (exceções)
        self.english_exceptions = {
            "Lua", "Python", "C++", "OTClient", "OTUI", "LuaJIT", "OpenGL",
            "API", "UI", "GUI", "IDE", "JSON", "XML", "HTML", "CSS", "JavaScript",
            "Git", "GitHub", "README", "LICENSE", "CMake", "Makefile",
            "Windows", "Linux", "macOS", "Android", "iOS"
        }
    
    def check_file_consistency(self, file_path):
        """Verifica consistência de idioma em um arquivo específico."""
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
        except Exception as e:
            return {
                "file": str(file_path),
                "error": f"Erro ao ler arquivo: {e}",
                "issues": []
            }
        
        issues = []
        
        # Verificar termos técnicos em inglês que deveriam estar em português
        for english_term, portuguese_term in self.technical_terms.items():
            # Buscar o termo em inglês (case insensitive)
            pattern = r'\b' + re.escape(english_term) + r'\b'
            matches = re.finditer(pattern, content, re.IGNORECASE)
            
            for match in matches:
                # Verificar se não é uma exceção
                if english_term.lower() not in [exc.lower() for exc in self.english_exceptions]:
                    issues.append({
                        "type": "termo_ingles",
                        "term": english_term,
                        "sugestao": portuguese_term,
                        "linha": content[:match.start()].count('\n') + 1,
                        "contexto": content[max(0, match.start()-20):match.end()+20]
                    })
        
        # Verificar inconsistências de capitalização
        for term in self.technical_terms.values():
            if term.lower() in content.lower():
                # Verificar se há variações de capitalização
                pattern = r'\b' + re.escape(term) + r'\b'
                matches = re.finditer(pattern, content, re.IGNORECASE)
                
                for match in matches:
                    if match.group() != term:
                        issues.append({
                            "type": "capitalizacao",
                            "term": match.group(),
                            "sugestao": term,
                            "linha": content[:match.start()].count('\n') + 1,
                            "contexto": content[max(0, match.start()-20):match.end()+20]
                        })
        
        return {
            "file": str(file_path),
            "issues": issues,
            "total_issues": len(issues)
        }
    
    def check_all_files(self):
        """Verifica consistência em todos os arquivos markdown da wiki."""
        results = []
        total_issues = 0
        
        # Buscar todos os arquivos .md na wiki
        for file_path in self.wiki_path.rglob("*.md"):
            if file_path.name.startswith('.'):
                continue  # Pular arquivos ocultos
                
            result = self.check_file_consistency(file_path)
            results.append(result)
            total_issues += result.get("total_issues", 0)
        
        return {
            "metadata": {
                "timestamp": datetime.now().isoformat(),
                "total_files": len(results),
                "total_issues": total_issues,
                "description": "Relatório de consistência de idioma da wiki"
            },
            "files": results,
            "summary": {
                "files_with_issues": len([r for r in results if r.get("total_issues", 0) > 0]),
                "files_clean": len([r for r in results if r.get("total_issues", 0) == 0]),
                "most_common_issues": self.get_most_common_issues(results)
            }
        }
    
    def get_most_common_issues(self, results):
        """Identifica os problemas mais comuns."""
        issue_counts = {}
        
        for result in results:
            for issue in result.get("issues", []):
                issue_type = issue.get("type", "desconhecido")
                term = issue.get("term", "desconhecido")
                key = f"{issue_type}:{term}"
                issue_counts[key] = issue_counts.get(key, 0) + 1
        
        # Ordenar por frequência
        sorted_issues = sorted(issue_counts.items(), key=lambda x: x[1], reverse=True)
        return sorted_issues[:10]  # Top 10
    
    def generate_report(self):
        """Gera relatório completo de consistência."""
        print("🔍 Verificando consistência de idioma na wiki...")
        
        report = self.check_all_files()
        
        # Salvar relatório
        with open(self.report_path, 'w', encoding='utf-8') as f:
            json.dump(report, f, indent=2, ensure_ascii=False)
        
        # Exibir resumo
        print(f"\n📊 RELATÓRIO DE CONSISTÊNCIA DE IDIOMA")
        print(f"📁 Arquivos verificados: {report['metadata']['total_files']}")
        print(f"❌ Total de problemas: {report['metadata']['total_issues']}")
        print(f"🔧 Arquivos com problemas: {report['summary']['files_with_issues']}")
        print(f"✅ Arquivos limpos: {report['summary']['files_clean']}")
        
        if report['summary']['most_common_issues']:
            print(f"\n🔍 PROBLEMAS MAIS COMUNS:")
            for issue, count in report['summary']['most_common_issues']:
                print(f"  - {issue}: {count} ocorrências")
        
        print(f"\n📄 Relatório salvo em: {self.report_path}")
        
        return report

def main():
    """Função principal."""
    checker = LanguageConsistencyChecker()
    report = checker.generate_report()
    
    # Retornar código de saída baseado no número de problemas
    if report['metadata']['total_issues'] == 0:
        print("\n✅ Nenhum problema de consistência encontrado!")
        return 0
    else:
        print(f"\n⚠️  {report['metadata']['total_issues']} problemas de consistência encontrados.")
        return 1

if __name__ == "__main__":
    exit(main()) 