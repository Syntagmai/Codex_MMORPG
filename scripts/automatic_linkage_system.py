#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Sistema de Linkagem Automática - Task 20.4
Implementa sistema que automaticamente cria links base para novos arquivos
"""

import json
import re
import os
from datetime import datetime
from pathlib import Path
from typing import Dict, List, Tuple, Optional

class AutomaticLinkageSystem:
    def __init__(self):
        self.wiki_path = Path("wiki")
        self.maps_path = self.wiki_path / "maps"
        self.templates_path = self.wiki_path / "templates"
        
    def load_category_hierarchy(self) -> Dict:
        """Carrega a hierarquia de categorias"""
        hierarchy_file = self.maps_path / "category_hierarchy.json"
        with open(hierarchy_file, 'r', encoding='utf-8') as f:
            return json.load(f)
    
    def load_files_categorized(self) -> Dict:
        """Carrega arquivos categorizados"""
        files_file = self.maps_path / "files_categorized.json"
        with open(files_file, 'r', encoding='utf-8') as f:
            return json.load(f)
    
    def detect_file_category(self, file_path: Path) -> str:
        """Detecta a categoria de um arquivo baseado no caminho"""
        hierarchy = self.load_category_hierarchy()
        files_categorized = self.load_files_categorized()
        
        # Converter caminho para string relativa
        relative_path = str(file_path.relative_to(self.wiki_path))
        
        # Verificar se arquivo já está categorizado
        if relative_path in files_categorized:
            return files_categorized[relative_path].get('category', 'Documentation')
        
        # Detectar categoria baseada no caminho
        path_parts = relative_path.lower().split('/')
        
        # Mapeamento de caminhos para categorias
        path_to_category = {
            'dashboard': 'Task_Management',
            'bmad': 'BMAD_System',
            'habdel': 'Research',
            'integration': 'Integration',
            'tools': 'Tools',
            'update': 'Tools',
            'maps': 'Tools',
            'docs': 'Documentation',
            'otclient': 'Core',
            'modules': 'Core',
            'src': 'Core',
            'legacy': 'Legacy',
            'backup': 'Legacy'
        }
        
        for part in path_parts:
            if part in path_to_category:
                return path_to_category[part]
        
        # Categorias baseadas em palavras-chave no nome do arquivo
        filename = file_path.name.lower()
        
        if any(word in filename for word in ['game', 'combat', 'item', 'creature', 'world']):
            return 'Game_Systems'
        elif any(word in filename for word in ['ui', 'otui', 'interface', 'graphic', 'animation']):
            return 'UI_Systems'
        elif any(word in filename for word in ['api', 'development', 'code', 'example', 'guide']):
            return 'Development'
        elif any(word in filename for word in ['agent', 'workflow', 'automation', 'template']):
            return 'BMAD_System'
        elif any(word in filename for word in ['task', 'epic', 'report', 'dashboard']):
            return 'Task_Management'
        elif any(word in filename for word in ['integration', 'canary', 'protocol', 'migration']):
            return 'Integration'
        elif any(word in filename for word in ['research', 'analysis', 'study', 'habdel']):
            return 'Research'
        elif any(word in filename for word in ['guide', 'reference', 'faq', 'glossary', 'troubleshooting']):
            return 'Documentation'
        elif any(word in filename for word in ['tool', 'script', 'analysis', 'validation']):
            return 'Tools'
        elif any(word in filename for word in ['legacy', 'old', 'backup', 'archive']):
            return 'Legacy'
        
        return 'Documentation'  # Categoria padrão
    
    def get_required_links(self, category: str) -> List[str]:
        """Retorna links obrigatórios para uma categoria"""
        base_links = [
            "[[../README|Hub Central da Wiki]]",
            "[[../dashboard/task_master|Task Master]]",
            "[[../dashboard/integrated_task_manager|Dashboard Central]]"
        ]
        
        # Links específicos por categoria
        category_specific_links = {
            'Core': [
                "[[../maps/otclient_source_index|Índice do Código-Fonte]]",
                "[[../maps/modules_index|Índice de Módulos]]"
            ],
            'Game_Systems': [
                "[[../maps/search_index|Busca por Sistemas de Jogo]]",
                "[[../maps/tags_index|Tags de Game Systems]]"
            ],
            'UI_Systems': [
                "[[../maps/styles_index|Índice de Estilos]]",
                "[[../maps/search_index|Busca por UI Systems]]"
            ],
            'Development': [
                "[[../maps/code_examples_analysis|Análise de Exemplos]]",
                "[[../maps/search_index|Busca por Desenvolvimento]]"
            ],
            'BMAD_System': [
                "[[../bmad/README|Sistema BMAD]]",
                "[[../maps/bmad_agents_index|Índice de Agentes]]"
            ],
            'Task_Management': [
                "[[../dashboard/task_master|Task Master]]",
                "[[../dashboard/integrated_task_manager|Dashboard Central]]"
            ],
            'Integration': [
                "[[../integration/README|Sistema de Integração]]",
                "[[../maps/canary_integration_map|Mapa de Integração Canary]]"
            ],
            'Research': [
                "[[../habdel/README|Sistema Habdel]]",
                "[[../maps/habdel_index|Índice Habdel]]"
            ],
            'Documentation': [
                "[[../maps/search_index|Índice de Busca]]",
                "[[../maps/tags_index|Índice de Tags]]"
            ],
            'Tools': [
                "[[../maps/tools_index|Índice de Ferramentas]]",
                "[[../update/README|Scripts de Atualização]]"
            ],
            'Legacy': [
                "[[../maps/search_index|Busca em Arquivos Legados]]",
                "[[../legacy_docs/README|Documentação Legada]]"
            ]
        }
        
        return base_links + category_specific_links.get(category, [])
    
    def get_navigation_links(self) -> List[str]:
        """Retorna links de navegação padrão"""
        return [
            "[[../maps/search_index|Índice de Busca]]",
            "[[../maps/tags_index|Índice de Tags]]",
            "[[../maps/category_indices|Índices por Categoria]]",
            "[[../maps/relationships|Relacionamentos]]"
        ]
    
    def create_automatic_links(self, file_path: Path) -> str:
        """Cria links automáticos para um arquivo"""
        category = self.detect_file_category(file_path)
        required_links = self.get_required_links(category)
        navigation_links = self.get_navigation_links()
        
        # Criar seção de links automáticos
        links_section = f"""## 🔗 **Links Automáticos**

> [!info] **Links Gerados Automaticamente**
> Estes links foram criados automaticamente pelo sistema de linkagem da categoria **{category}**

### **📚 Links Obrigatórios**
"""
        
        for link in required_links:
            links_section += f"- {link}\n"
        
        links_section += "\n### **🧭 Navegação**\n"
        
        for link in navigation_links:
            links_section += f"- {link}\n"
        
        links_section += f"""
### **📊 Métricas da Categoria**
- **Categoria**: {category}
- **Total de arquivos**: <!-- Contador automático -->
- **Arquivos linkados**: <!-- Contador automático -->
- **Taxa de linkagem**: <!-- Percentual automático -->

---

"""
        
        return links_section
    
    def apply_automatic_links_to_file(self, file_path: Path) -> bool:
        """Aplica links automáticos a um arquivo específico"""
        try:
            # Ler conteúdo atual
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # Verificar se já tem links automáticos
            if "## 🔗 **Links Automáticos**" in content:
                print(f"⚠️ Arquivo já possui links automáticos: {file_path}")
                return False
            
            # Criar links automáticos
            automatic_links = self.create_automatic_links(file_path)
            
            # Adicionar links ao final do arquivo (antes de qualquer seção de links existente)
            if "## 🔗" in content:
                # Inserir antes da primeira seção de links
                pattern = r"(## 🔗.*?)(?=\n## |\n---|\n$)"
                content = re.sub(pattern, automatic_links + r"\1", content, flags=re.DOTALL)
            else:
                # Adicionar ao final
                content += "\n" + automatic_links
            
            # Salvar arquivo atualizado
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(content)
            
            print(f"✅ Links automáticos aplicados: {file_path}")
            return True
            
        except Exception as e:
            print(f"❌ Erro ao aplicar links automáticos em {file_path}: {e}")
            return False
    
    def scan_and_link_new_files(self) -> Dict:
        """Escaneia e aplica links automáticos a novos arquivos"""
        print("🔄 Escaneando arquivos para linkagem automática...")
        
        # Carregar arquivos já processados
        processed_file = self.maps_path / "automatic_links_processed.json"
        processed_files = set()
        
        if processed_file.exists():
            with open(processed_file, 'r', encoding='utf-8') as f:
                data = json.load(f)
                processed_files = set(data.get('processed_files', []))
        
        # Encontrar todos os arquivos markdown na wiki
        markdown_files = list(self.wiki_path.rglob("*.md"))
        
        # Filtrar arquivos não processados
        new_files = []
        for file_path in markdown_files:
            relative_path = str(file_path.relative_to(self.wiki_path))
            if relative_path not in processed_files:
                new_files.append(file_path)
        
        print(f"📋 Encontrados {len(new_files)} arquivos novos para processar")
        
        # Aplicar links automáticos
        processed_count = 0
        failed_count = 0
        
        for file_path in new_files:
            if self.apply_automatic_links_to_file(file_path):
                processed_count += 1
                processed_files.add(str(file_path.relative_to(self.wiki_path)))
            else:
                failed_count += 1
        
        # Salvar lista de arquivos processados
        with open(processed_file, 'w', encoding='utf-8') as f:
            json.dump({
                'timestamp': datetime.now().isoformat(),
                'processed_files': list(processed_files),
                'total_processed': len(processed_files)
            }, f, indent=2, ensure_ascii=False)
        
        # Gerar relatório
        report = {
            'timestamp': datetime.now().isoformat(),
            'files_scanned': len(markdown_files),
            'new_files_found': len(new_files),
            'files_processed': processed_count,
            'files_failed': failed_count,
            'total_processed': len(processed_files),
            'status': 'success'
        }
        
        report_file = self.maps_path / "automatic_linkage_report.json"
        with open(report_file, 'w', encoding='utf-8') as f:
            json.dump(report, f, indent=2, ensure_ascii=False)
        
        print(f"✅ Processamento concluído:")
        print(f"   📄 Arquivos escaneados: {len(markdown_files)}")
        print(f"   🆕 Arquivos novos: {len(new_files)}")
        print(f"   ✅ Processados com sucesso: {processed_count}")
        print(f"   ❌ Falharam: {failed_count}")
        print(f"   📊 Total processados: {len(processed_files)}")
        
        return report
    
    def create_linkage_rules(self) -> Dict:
        """Cria regras de linkagem por categoria"""
        hierarchy = self.load_category_hierarchy()
        
        rules = {}
        for category_name, category_data in hierarchy.items():
            rules[category_name] = {
                'description': category_data.get('description', ''),
                'required_links': self.get_required_links(category_name),
                'navigation_links': self.get_navigation_links(),
                'priority': self.get_category_priority(category_name),
                'auto_link': True
            }
        
        # Salvar regras
        rules_file = self.maps_path / "linkage_rules.json"
        with open(rules_file, 'w', encoding='utf-8') as f:
            json.dump(rules, f, indent=2, ensure_ascii=False)
        
        print(f"✅ Regras de linkagem criadas: {len(rules)} categorias")
        return rules
    
    def get_category_priority(self, category: str) -> str:
        """Retorna prioridade de uma categoria"""
        high_priority = ['Core', 'Game_Systems', 'Development', 'Task_Management']
        medium_priority = ['UI_Systems', 'BMAD_System', 'Integration', 'Documentation']
        
        if category in high_priority:
            return 'Alta'
        elif category in medium_priority:
            return 'Média'
        else:
            return 'Baixa'
    
    def validate_links(self, file_path: Path) -> Dict:
        """Valida links em um arquivo"""
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # Encontrar todos os links markdown
            link_pattern = r'\[\[([^\]]+)\]\]'
            links = re.findall(link_pattern, content)
            
            valid_links = []
            invalid_links = []
            
            for link in links:
                # Extrair caminho do arquivo
                if '|' in link:
                    file_part = link.split('|')[0]
                else:
                    file_part = link
                
                # Verificar se arquivo existe
                if file_part.startswith('../'):
                    target_path = self.wiki_path / file_part[3:]
                else:
                    target_path = file_path.parent / file_part
                
                if target_path.exists():
                    valid_links.append(link)
                else:
                    invalid_links.append(link)
            
            return {
                'file': str(file_path),
                'total_links': len(links),
                'valid_links': len(valid_links),
                'invalid_links': len(invalid_links),
                'valid_links_list': valid_links,
                'invalid_links_list': invalid_links
            }
            
        except Exception as e:
            return {
                'file': str(file_path),
                'error': str(e),
                'total_links': 0,
                'valid_links': 0,
                'invalid_links': 0
            }

def main():
    """Função principal"""
    system = AutomaticLinkageSystem()
    
    print("🎯 **Task 20.4 - Sistema de Links Automáticos**")
    print("🔄 Iniciando sistema de linkagem automática...")
    
    # Criar regras de linkagem
    print("\n📋 Criando regras de linkagem...")
    rules = system.create_linkage_rules()
    
    # Escanear e aplicar links automáticos
    print("\n🔍 Escaneando arquivos para linkagem...")
    report = system.scan_and_link_new_files()
    
    print(f"\n✅ **Task 20.4 - Sub-tarefa 2 Concluída**")
    print("✅ Script de linkagem automática implementado")
    print("✅ Regras de linkagem por categoria criadas")
    print("✅ Sistema de validação de links implementado")
    print("📋 Próximo passo: Criar sistema de notificação de arquivos órfãos")

if __name__ == "__main__":
    main() 