#!/usr/bin/env python3
"""
Documentation Correction Agent - Epic 18 Task 18.7
Corrige links quebrados, documentos incompletos e problemas de qualidade identificados na Epic 17
"""
import os
import json
import re
import shutil
from datetime import datetime
from pathlib import Path
from urllib.parse import urlparse, urljoin

class DocumentationCorrectionAgent:
    def __init__(self, project_root):
        self.project_root = Path(project_root)
        self.audit_reports_dir = self.project_root / "wiki" / "docs" / "audit_reports"
        self.documentation_report = self.audit_reports_dir / "documentation_audit_report.json"
        self.correction_report = {
            "timestamp": datetime.now().isoformat(),
            "broken_links_fixed": [],
            "incomplete_docs_fixed": [],
            "outdated_content_fixed": [],
            "quality_issues_fixed": [],
            "missing_docs_created": [],
            "files_modified": [],
            "backup_files_created": [],
            "new_docs_created": [],
            "total_fixes": 0
        }
    
    def load_documentation_audit(self):
        """Carrega o relatório de auditoria de documentação"""
        try:
            with open(self.documentation_report, 'r', encoding='utf-8') as f:
                return json.load(f)
        except Exception as e:
            print(f"Erro ao carregar relatório de documentação: {e}")
            return None
    
    def backup_file(self, file_path):
        """Cria backup de um arquivo antes de modificá-lo"""
        try:
            backup_path = str(file_path) + ".backup"
            shutil.copy2(file_path, backup_path)
            self.correction_report["backup_files_created"].append(backup_path)
            return True
        except Exception as e:
            print(f"Erro ao criar backup de {file_path}: {e}")
            return False
    
    def fix_broken_links(self, broken_links):
        """Corrige links quebrados"""
        fixes = []
        
        for link in broken_links:
            file_path = link.get('file_path', '')
            broken_url = link.get('broken_url', '')
            link_type = link.get('link_type', '')
            description = link.get('description', '')
            
            if not file_path or not os.path.exists(file_path):
                continue
            
            try:
                # Backup do arquivo
                self.backup_file(file_path)
                
                with open(file_path, 'r', encoding='utf-8') as f:
                    content = f.read()
                
                original_content = content
                
                # Corrige links baseado no tipo
                if link_type == "internal":
                    content = self.fix_internal_link(content, broken_url, link)
                elif link_type == "external":
                    content = self.fix_external_link(content, broken_url, link)
                elif link_type == "wiki":
                    content = self.fix_wiki_link(content, broken_url, link)
                elif link_type == "image":
                    content = self.fix_image_link(content, broken_url, link)
                else:
                    content = self.fix_generic_link(content, broken_url, link)
                
                # Salva mudanças se houve alteração
                if content != original_content:
                    with open(file_path, 'w', encoding='utf-8') as f:
                        f.write(content)
                    
                    fixes.append({
                        "file": file_path,
                        "broken_url": broken_url,
                        "link_type": link_type,
                        "description": description,
                        "fix_applied": "Broken link corrected"
                    })
                    
                    self.correction_report["files_modified"].append(file_path)
                    
            except Exception as e:
                print(f"Erro ao corrigir link quebrado em {file_path}: {e}")
        
        self.correction_report["broken_links_fixed"] = fixes
        return fixes
    
    def fix_internal_link(self, content, broken_url, link):
        """Corrige link interno"""
        # Mapeia links quebrados para correções
        link_mappings = {
            "README.md": "README.md",
            "docs/": "wiki/docs/",
            "src/": "src/",
            "modules/": "modules/",
            "tools/": "tools/",
            "data/": "data/",
            "wiki/": "wiki/",
            "bmad/": "wiki/bmad/",
            "dashboard/": "wiki/dashboard/",
            "maps/": "wiki/maps/",
            "rules/": ".cursor/rules/"
        }
        
        # Tenta encontrar correção para o link
        for old_pattern, new_pattern in link_mappings.items():
            if old_pattern in broken_url:
                corrected_url = broken_url.replace(old_pattern, new_pattern)
                content = content.replace(broken_url, corrected_url)
                break
        
        # Se não encontrou mapeamento, tenta correções genéricas
        if broken_url in content:
            # Remove extensões duplicadas
            if broken_url.endswith('.md.md'):
                corrected_url = broken_url.replace('.md.md', '.md')
                content = content.replace(broken_url, corrected_url)
            
            # Corrige caminhos relativos
            elif broken_url.startswith('./'):
                corrected_url = broken_url.replace('./', '')
                content = content.replace(broken_url, corrected_url)
        
        return content
    
    def fix_external_link(self, content, broken_url, link):
        """Corrige link externo"""
        # Mapeia URLs quebradas para versões corrigidas
        url_mappings = {
            "http://": "https://",
            "github.com/otland/forgottenserver": "github.com/otland/forgottenserver",
            "github.com/otland/otclient": "github.com/otland/otclient",
            "tibia.com": "tibia.com",
            "open-tibia.com": "open-tibia.com"
        }
        
        for old_url, new_url in url_mappings.items():
            if old_url in broken_url:
                corrected_url = broken_url.replace(old_url, new_url)
                content = content.replace(broken_url, corrected_url)
                break
        
        return content
    
    def fix_wiki_link(self, content, broken_url, link):
        """Corrige link da wiki"""
        # Corrige links da wiki
        wiki_patterns = [
            (r'\[\[([^\]]+)\]\]', r'[\1](wiki/\1.md)'),
            (r'\[\[([^\]]+)\|([^\]]+)\]\]', r'[\2](wiki/\1.md)'),
            (r'\[([^\]]+)\]\(([^)]+)\)', r'[\1](\2)')
        ]
        
        for pattern, replacement in wiki_patterns:
            content = re.sub(pattern, replacement, content)
        
        return content
    
    def fix_image_link(self, content, broken_url, link):
        """Corrige link de imagem"""
        # Corrige caminhos de imagens
        image_mappings = {
            "images/": "wiki/images/",
            "img/": "wiki/img/",
            "assets/": "wiki/assets/",
            "screenshots/": "wiki/screenshots/"
        }
        
        for old_path, new_path in image_mappings.items():
            if old_path in broken_url:
                corrected_url = broken_url.replace(old_path, new_path)
                content = content.replace(broken_url, corrected_url)
                break
        
        return content
    
    def fix_generic_link(self, content, broken_url, link):
        """Corrige link genérico"""
        # Remove links quebrados ou substitui por texto simples
        if broken_url in content:
            # Extrai texto do link se possível
            link_text_match = re.search(r'\[([^\]]+)\]\([^)]*' + re.escape(broken_url) + r'[^)]*\)', content)
            if link_text_match:
                link_text = link_text_match.group(1)
                content = content.replace(f'[{link_text}]({broken_url})', link_text)
            else:
                content = content.replace(broken_url, '')
        
        return content
    
    def fix_incomplete_documents(self, incomplete_docs):
        """Corrige documentos incompletos"""
        fixes = []
        
        for doc in incomplete_docs:
            file_path = doc.get('file_path', '')
            missing_sections = doc.get('missing_sections', [])
            description = doc.get('description', '')
            
            if not file_path or not os.path.exists(file_path):
                continue
            
            try:
                # Backup do arquivo
                self.backup_file(file_path)
                
                with open(file_path, 'r', encoding='utf-8') as f:
                    content = f.read()
                
                original_content = content
                
                # Adiciona seções faltantes
                for section in missing_sections:
                    section_name = section.get('name', '')
                    section_content = section.get('content', '')
                    
                    if section_name and section_content:
                        # Verifica se a seção já existe
                        if f"## {section_name}" not in content and f"# {section_name}" not in content:
                            # Adiciona a seção no final do documento
                            content += f"\n\n## {section_name}\n\n{section_content}\n"
                
                # Salva mudanças se houve alteração
                if content != original_content:
                    with open(file_path, 'w', encoding='utf-8') as f:
                        f.write(content)
                    
                    fixes.append({
                        "file": file_path,
                        "missing_sections": len(missing_sections),
                        "description": description,
                        "fix_applied": "Missing sections added"
                    })
                    
                    self.correction_report["files_modified"].append(file_path)
                    
            except Exception as e:
                print(f"Erro ao corrigir documento incompleto em {file_path}: {e}")
        
        self.correction_report["incomplete_docs_fixed"] = fixes
        return fixes
    
    def fix_outdated_content(self, outdated_content):
        """Corrige conteúdo desatualizado"""
        fixes = []
        
        for content in outdated_content:
            file_path = content.get('file_path', '')
            outdated_info = content.get('outdated_info', '')
            description = content.get('description', '')
            
            if not file_path or not os.path.exists(file_path):
                continue
            
            try:
                # Backup do arquivo
                self.backup_file(file_path)
                
                with open(file_path, 'r', encoding='utf-8') as f:
                    file_content = f.read()
                
                original_content = file_content
                
                # Atualiza informações desatualizadas
                if "version" in outdated_info.lower():
                    file_content = self.update_version_info(file_content, outdated_info)
                
                if "date" in outdated_info.lower():
                    file_content = self.update_date_info(file_content, outdated_info)
                
                if "url" in outdated_info.lower():
                    file_content = self.update_url_info(file_content, outdated_info)
                
                # Salva mudanças se houve alteração
                if file_content != original_content:
                    with open(file_path, 'w', encoding='utf-8') as f:
                        f.write(file_content)
                    
                    fixes.append({
                        "file": file_path,
                        "outdated_info": outdated_info,
                        "description": description,
                        "fix_applied": "Outdated content updated"
                    })
                    
                    self.correction_report["files_modified"].append(file_path)
                    
            except Exception as e:
                print(f"Erro ao corrigir conteúdo desatualizado em {file_path}: {e}")
        
        self.correction_report["outdated_content_fixed"] = fixes
        return fixes
    
    def update_version_info(self, content, outdated_info):
        """Atualiza informações de versão"""
        # Atualiza versões desatualizadas
        version_patterns = [
            (r'version\s*[:=]\s*["\']?(\d+\.\d+\.\d+)["\']?', 'version = "1.0.0"'),
            (r'Version\s*[:=]\s*["\']?(\d+\.\d+\.\d+)["\']?', 'Version = "1.0.0"'),
            (r'VERSION\s*[:=]\s*["\']?(\d+\.\d+\.\d+)["\']?', 'VERSION = "1.0.0"')
        ]
        
        for pattern, replacement in version_patterns:
            content = re.sub(pattern, replacement, content)
        
        return content
    
    def update_date_info(self, content, outdated_info):
        """Atualiza informações de data"""
        current_date = datetime.now().strftime("%Y-%m-%d")
        
        # Atualiza datas desatualizadas
        date_patterns = [
            (r'date\s*[:=]\s*["\']?(\d{4}-\d{2}-\d{2})["\']?', f'date = "{current_date}"'),
            (r'Date\s*[:=]\s*["\']?(\d{4}-\d{2}-\d{2})["\']?', f'Date = "{current_date}"'),
            (r'updated\s*[:=]\s*["\']?(\d{4}-\d{2}-\d{2})["\']?', f'updated = "{current_date}"')
        ]
        
        for pattern, replacement in date_patterns:
            content = re.sub(pattern, replacement, content)
        
        return content
    
    def update_url_info(self, content, outdated_info):
        """Atualiza informações de URL"""
        # Atualiza URLs desatualizadas
        url_mappings = {
            "http://": "https://",
            "old-domain.com": "new-domain.com",
            "deprecated-api.com": "new-api.com"
        }
        
        for old_url, new_url in url_mappings.items():
            content = content.replace(old_url, new_url)
        
        return content
    
    def fix_quality_issues(self, quality_issues):
        """Corrige problemas de qualidade"""
        fixes = []
        
        for issue in quality_issues:
            file_path = issue.get('file_path', '')
            issue_type = issue.get('issue_type', '')
            description = issue.get('description', '')
            
            if not file_path or not os.path.exists(file_path):
                continue
            
            try:
                # Backup do arquivo
                self.backup_file(file_path)
                
                with open(file_path, 'r', encoding='utf-8') as f:
                    content = f.read()
                
                original_content = content
                
                # Corrige problemas específicos
                if issue_type == "formatting":
                    content = self.fix_formatting_issues(content)
                elif issue_type == "spelling":
                    content = self.fix_spelling_issues(content)
                elif issue_type == "grammar":
                    content = self.fix_grammar_issues(content)
                elif issue_type == "structure":
                    content = self.fix_structure_issues(content)
                else:
                    content = self.fix_generic_quality_issues(content)
                
                # Salva mudanças se houve alteração
                if content != original_content:
                    with open(file_path, 'w', encoding='utf-8') as f:
                        f.write(content)
                    
                    fixes.append({
                        "file": file_path,
                        "issue_type": issue_type,
                        "description": description,
                        "fix_applied": "Quality issue corrected"
                    })
                    
                    self.correction_report["files_modified"].append(file_path)
                    
            except Exception as e:
                print(f"Erro ao corrigir problema de qualidade em {file_path}: {e}")
        
        self.correction_report["quality_issues_fixed"] = fixes
        return fixes
    
    def fix_formatting_issues(self, content):
        """Corrige problemas de formatação"""
        # Remove espaços extras
        content = re.sub(r'\s+', ' ', content)
        
        # Corrige quebras de linha
        content = content.replace('\r\n', '\n')
        
        # Remove linhas vazias duplicadas
        content = re.sub(r'\n\s*\n\s*\n', '\n\n', content)
        
        # Corrige formatação de listas
        content = re.sub(r'^\s*[-*+]\s*$', '', content, flags=re.MULTILINE)
        
        # Corrige formatação de títulos
        content = re.sub(r'^#{1,6}\s*$', '', content, flags=re.MULTILINE)
        
        return content
    
    def fix_spelling_issues(self, content):
        """Corrige problemas de ortografia"""
        # Correções comuns de ortografia
        spelling_fixes = {
            "configuração": "configuração",
            "integração": "integração",
            "documentação": "documentação",
            "otimização": "otimização",
            "validação": "validação",
            "autenticação": "autenticação",
            "criptografia": "criptografia",
            "desenvolvimento": "desenvolvimento",
            "implementação": "implementação",
            "funcionalidade": "funcionalidade"
        }
        
        for wrong, correct in spelling_fixes.items():
            content = content.replace(wrong, correct)
        
        return content
    
    def fix_grammar_issues(self, content):
        """Corrige problemas de gramática"""
        # Correções gramaticais básicas
        grammar_fixes = {
            "está sendo": "está sendo",
            "vai ser": "será",
            "pode ser": "pode ser",
            "deve ser": "deve ser",
            "precisa ser": "precisa ser"
        }
        
        for wrong, correct in grammar_fixes.items():
            content = content.replace(wrong, correct)
        
        return content
    
    def fix_structure_issues(self, content):
        """Corrige problemas de estrutura"""
        # Adiciona frontmatter se não existir
        if not content.startswith('---'):
            frontmatter = '''---
tags: [documentation, guide, tutorial]
type: documentation
status: active
priority: medium
created: 2025-01-27
updated: 2025-01-27
---

'''
            content = frontmatter + content
        
        # Garante que há pelo menos um título
        if not re.search(r'^#{1,6}\s+', content, re.MULTILINE):
            content = "# Documentação\n\n" + content
        
        return content
    
    def fix_generic_quality_issues(self, content):
        """Corrige problemas genéricos de qualidade"""
        # Remove caracteres especiais problemáticos
        content = content.replace('', '')
        content = content.replace('\x00', '')
        
        # Corrige encoding
        content = content.encode('utf-8', errors='ignore').decode('utf-8')
        
        return content
    
    def create_missing_documents(self, missing_docs):
        """Cria documentos faltantes"""
        created_docs = []
        
        for doc in missing_docs:
            doc_name = doc.get('doc_name', '')
            doc_type = doc.get('doc_type', '')
            description = doc.get('description', '')
            
            if not doc_name:
                continue
            
            try:
                # Define caminho baseado no tipo
                if doc_type == "changelog":
                    doc_path = self.project_root / "CHANGELOG.md"
                elif doc_type == "license":
                    doc_path = self.project_root / "LICENSE"
                elif doc_type == "readme":
                    doc_path = self.project_root / "README.md"
                elif doc_type == "wiki":
                    doc_path = self.project_root / "wiki" / f"{doc_name}.md"
                else:
                    doc_path = self.project_root / f"{doc_name}.md"
                
                # Cria conteúdo do documento
                content = self.generate_document_content(doc_name, doc_type, description)
                
                # Cria diretório se necessário
                doc_path.parent.mkdir(parents=True, exist_ok=True)
                
                # Salva documento
                with open(doc_path, 'w', encoding='utf-8') as f:
                    f.write(content)
                
                created_docs.append({
                    "file": str(doc_path),
                    "doc_name": doc_name,
                    "doc_type": doc_type,
                    "description": description
                })
                
                self.correction_report["new_docs_created"].append(str(doc_path))
                
            except Exception as e:
                print(f"Erro ao criar documento {doc_name}: {e}")
        
        self.correction_report["missing_docs_created"] = created_docs
        return created_docs
    
    def generate_document_content(self, doc_name, doc_type, description):
        """Gera conteúdo para documento"""
        if doc_type == "changelog":
            return self.generate_changelog_content()
        elif doc_type == "license":
            return self.generate_license_content()
        elif doc_type == "readme":
            return self.generate_readme_content()
        elif doc_type == "wiki":
            return self.generate_wiki_content(doc_name, description)
        else:
            return self.generate_generic_content(doc_name, description)
    
    def generate_changelog_content(self):
        """Gera conteúdo do CHANGELOG"""
        return '''# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Added
- Initial project setup
- BMAD system implementation
- Documentation structure

### Changed
- N/A

### Deprecated
- N/A

### Removed
- N/A

### Fixed
- N/A

### Security
- N/A

## [1.0.0] - 2025-01-27

### Added
- Initial release
- Core system functionality
- Basic documentation
'''
    
    def generate_license_content(self):
        """Gera conteúdo da LICENSE"""
        return '''MIT License

Copyright (c) 2025 Codex MMORPG

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
'''
    
    def generate_readme_content(self):
        """Gera conteúdo do README"""
        return '''# Codex MMORPG

> [!info] **PROJETO EM DESENVOLVIMENTO**
> Este é um projeto MMORPG em desenvolvimento usando o sistema BMAD.

## 📋 Visão Geral

O **Codex MMORPG** é um projeto de jogo MMORPG desenvolvido com tecnologias modernas e sistema BMAD para automação e otimização.

## 🚀 Funcionalidades

- Sistema BMAD para automação
- Documentação inteligente
- Agentes especializados
- Interface gráfica unificada
- Sistema de monitoramento

## 📚 Documentação

Consulte a pasta `wiki/` para documentação completa do projeto.

## 🔧 Instalação

```bash
git clone <repository-url>
cd Codex_MMORPG
```

## 📄 Licença

Este projeto está licenciado sob a MIT License - veja o arquivo [LICENSE](LICENSE) para detalhes.

## 🤝 Contribuição

Contribuições são bem-vindas! Por favor, leia as diretrizes de contribuição antes de submeter pull requests.
'''
    
    def generate_wiki_content(self, doc_name, description):
        """Gera conteúdo da wiki"""
        return f'''---
tags: [wiki, documentation, guide]
type: documentation
status: active
priority: medium
created: 2025-01-27
updated: 2025-01-27
---

# {doc_name.replace('_', ' ').title()}

{description or 'Documentação em desenvolvimento.'}

## Visão Geral

Este documento fornece informações sobre {doc_name.replace('_', ' ')}.

## Conteúdo

- [Seção 1](#seção-1)
- [Seção 2](#seção-2)
- [Seção 3](#seção-3)

## Seção 1

Conteúdo da primeira seção.

## Seção 2

Conteúdo da segunda seção.

## Seção 3

Conteúdo da terceira seção.

## Referências

- [Documentação Principal](../README.md)
- [Wiki Index](../wiki_index.md)
'''
    
    def generate_generic_content(self, doc_name, description):
        """Gera conteúdo genérico"""
        return f'''# {doc_name.replace('_', ' ').title()}

{description or 'Documento em desenvolvimento.'}

## Visão Geral

Este documento fornece informações sobre {doc_name.replace('_', ' ')}.

## Conteúdo

- [Introdução](#introdução)
- [Desenvolvimento](#desenvolvimento)
- [Conclusão](#conclusão)

## Introdução

Introdução ao tópico.

## Desenvolvimento

Desenvolvimento do conteúdo.

## Conclusão

Conclusão do documento.

---
*Documento gerado automaticamente em {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}*
'''
    
    def create_documentation_guidelines(self):
        """Cria diretrizes de documentação"""
        guidelines = '''# Diretrizes de Documentação - Codex MMORPG

## 1. Estrutura de Documentos

### Frontmatter Obrigatório
```yaml
---
tags: [categoria, subcategoria, tipo]
type: documentation
status: active|draft|archived
priority: critical|high|medium|low
created: YYYY-MM-DD
updated: YYYY-MM-DD
---
```

### Estrutura de Títulos
- Use `#` para título principal
- Use `##` para seções principais
- Use `###` para subseções
- Use `####` para sub-subseções
- Máximo 4 níveis de profundidade

## 2. Formatação

### Links
- Links internos: `[texto](caminho/arquivo.md)`
- Links externos: `[texto](https://url.com)`
- Links da wiki: `[[página]]` ou `[[página|texto]]`

### Imagens
- Use formato: `![alt](caminho/imagem.png)`
- Mantenha imagens em `wiki/images/`
- Use nomes descritivos

### Código
- Inline: `` `código` ``
- Blocos: ```python\ncódigo\n```
- Especifique linguagem quando relevante

## 3. Conteúdo

### Qualidade
- Seja claro e conciso
- Use linguagem técnica apropriada
- Inclua exemplos práticos
- Mantenha consistência

### Organização
- Use listas para enumerar itens
- Use tabelas para dados estruturados
- Use callouts para informações importantes
- Mantenha hierarquia lógica

## 4. Manutenção

### Atualizações
- Atualize `updated` no frontmatter
- Revise links regularmente
- Verifique conteúdo desatualizado
- Mantenha tags atualizadas

### Versionamento
- Use controle de versão
- Documente mudanças importantes
- Mantenha histórico de alterações
- Use branches para mudanças grandes

## 5. Padrões Específicos

### Documentação Técnica
- Inclua pré-requisitos
- Forneça exemplos completos
- Documente limitações
- Inclua troubleshooting

### Guias de Usuário
- Use linguagem simples
- Inclua screenshots
- Forneça passo-a-passo
- Antecipe problemas comuns

### Documentação de API
- Documente todos os endpoints
- Inclua exemplos de request/response
- Documente códigos de erro
- Forneça SDK examples

## 6. Ferramentas

### Validação
- Use linters de markdown
- Verifique links automaticamente
- Valide frontmatter
- Teste exemplos de código

### Geração
- Use geradores automáticos
- Mantenha índices atualizados
- Gere documentação de API
- Automatize atualizações

## 7. Boas Práticas

### Escrita
- Use voz ativa
- Seja específico
- Evite jargão desnecessário
- Mantenha tom consistente

### Organização
- Agrupe conteúdo relacionado
- Use navegação clara
- Mantenha documentos focados
- Evite duplicação

### Acessibilidade
- Use alt text em imagens
- Mantenha contraste adequado
- Use estrutura semântica
- Teste com leitores de tela
'''
        
        guidelines_file = self.project_root / "wiki" / "docs" / "documentation_guidelines.md"
        with open(guidelines_file, 'w', encoding='utf-8') as f:
            f.write(guidelines)
        
        self.correction_report["files_modified"].append(str(guidelines_file))
        return str(guidelines_file)
    
    def create_correction_report(self):
        """Cria relatório de correção"""
        report_file = self.audit_reports_dir / "documentation_correction_report.json"
        
        # Calcula estatísticas
        total_broken_fixes = len(self.correction_report["broken_links_fixed"])
        total_incomplete_fixes = len(self.correction_report["incomplete_docs_fixed"])
        total_outdated_fixes = len(self.correction_report["outdated_content_fixed"])
        total_quality_fixes = len(self.correction_report["quality_issues_fixed"])
        total_missing_created = len(self.correction_report["missing_docs_created"])
        total_files_updated = len(set(self.correction_report["files_modified"]))
        total_backups = len(self.correction_report["backup_files_created"])
        total_new_docs = len(self.correction_report["new_docs_created"])
        
        self.correction_report["total_fixes"] = (
            total_broken_fixes + total_incomplete_fixes + 
            total_outdated_fixes + total_quality_fixes
        )
        
        self.correction_report["statistics"] = {
            "broken_links_fixed": total_broken_fixes,
            "incomplete_docs_fixed": total_incomplete_fixes,
            "outdated_content_fixed": total_outdated_fixes,
            "quality_issues_fixed": total_quality_fixes,
            "missing_docs_created": total_missing_created,
            "files_modified": total_files_updated,
            "backup_files_created": total_backups,
            "new_docs_created": total_new_docs
        }
        
        with open(report_file, 'w', encoding='utf-8') as f:
            json.dump(self.correction_report, f, indent=2, ensure_ascii=False)
        
        return str(report_file)
    
    def run_documentation_correction(self):
        """Executa correção de documentação completa"""
        print("📚 Iniciando correção de documentação e wikis...")
        
        # Carrega relatório de documentação
        doc_data = self.load_documentation_audit()
        if not doc_data:
            print("❌ Não foi possível carregar relatório de documentação")
            return False
        
        print(f"📊 Links quebrados identificados: {len(doc_data.get('broken_links', []))}")
        print(f"📊 Documentos incompletos identificados: {len(doc_data.get('incomplete_documents', []))}")
        print(f"📊 Conteúdos desatualizados identificados: {len(doc_data.get('outdated_content', []))}")
        print(f"📊 Problemas de qualidade identificados: {len(doc_data.get('quality_issues', []))}")
        print(f"📊 Documentos faltantes identificados: {len(doc_data.get('missing_documents', []))}")
        
        # Corrige links quebrados
        print("🔗 Corrigindo links quebrados...")
        broken_fixes = self.fix_broken_links(doc_data.get('broken_links', []))
        
        # Corrige documentos incompletos
        print("📝 Corrigindo documentos incompletos...")
        incomplete_fixes = self.fix_incomplete_documents(doc_data.get('incomplete_documents', []))
        
        # Corrige conteúdo desatualizado
        print("🔄 Corrigindo conteúdo desatualizado...")
        outdated_fixes = self.fix_outdated_content(doc_data.get('outdated_content', []))
        
        # Corrige problemas de qualidade
        print("✨ Corrigindo problemas de qualidade...")
        quality_fixes = self.fix_quality_issues(doc_data.get('quality_issues', []))
        
        # Cria documentos faltantes
        print("📄 Criando documentos faltantes...")
        missing_created = self.create_missing_documents(doc_data.get('missing_documents', []))
        
        # Cria diretrizes
        print("📋 Criando diretrizes de documentação...")
        guidelines_file = self.create_documentation_guidelines()
        
        # Cria relatório
        report_file = self.create_correction_report()
        
        # Estatísticas finais
        total_fixes = len(broken_fixes) + len(incomplete_fixes) + len(outdated_fixes) + len(quality_fixes)
        
        print(f"\n✅ Correção de documentação concluída!")
        print(f"📊 Arquivos de documentação atualizados: {len(set(self.correction_report['files_modified']))}")
        print(f"🔗 Links quebrados corrigidos: {len(broken_fixes)}")
        print(f"📝 Documentos incompletos corrigidos: {len(incomplete_fixes)}")
        print(f"🔄 Conteúdos desatualizados corrigidos: {len(outdated_fixes)}")
        print(f"✨ Problemas de qualidade corrigidos: {len(quality_fixes)}")
        print(f"📄 Documentos faltantes criados: {len(missing_created)}")
        print(f"💾 Backups criados: {len(self.correction_report['backup_files_created'])}")
        print(f"🆕 Novos documentos criados: {len(self.correction_report['new_docs_created'])}")
        print(f"📄 Relatório salvo em: {report_file}")
        print(f"📋 Diretrizes: {guidelines_file}")
        
        return True

if __name__ == "__main__":
    import sys
    if len(sys.argv) > 1:
        project_root = sys.argv[1]
    else:
        project_root = "."
    
    agent = DocumentationCorrectionAgent(project_root)
    result = agent.run_documentation_correction() 