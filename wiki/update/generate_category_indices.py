#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script para gerar índices de categoria em markdown para Obsidian
Task 20.2 - Criar Sistema de Categorização Inteligente
"""

import json
from datetime import datetime
from pathlib import Path

class CategoryIndexGenerator:
    def __init__(self):
        self.wiki_path = Path("wiki")
        
    def load_categorization_data(self):
        """Carrega os dados de categorização."""
        # Carregar hierarquia de categorias
        hierarchy_path = self.wiki_path / "maps" / "category_hierarchy.json"
        if not hierarchy_path.exists():
            print("❌ Arquivo de hierarquia não encontrado. Execute primeiro o intelligent_categorization_system.py")
            return None, None
        
        with open(hierarchy_path, "r", encoding="utf-8") as f:
            hierarchy = json.load(f)
        
        # Carregar índices de categoria
        indices_path = self.wiki_path / "maps" / "category_indices.json"
        if not indices_path.exists():
            print("❌ Arquivo de índices não encontrado.")
            return hierarchy, None
        
        with open(indices_path, "r", encoding="utf-8") as f:
            indices = json.load(f)
        
        return hierarchy, indices
    
    def generate_main_category_index(self, hierarchy, indices):
        """Gera índice principal de categorias."""
        content = []
        content.append("# 📂 Índice Principal de Categorias")
        content.append("")
        content.append(f"*Gerado em: {datetime.now().strftime('%d/%m/%Y %H:%M:%S')}*")
        content.append("")
        content.append("## 📊 Resumo")
        content.append("")
        
        total_files = sum(indices[cat]["total_files"] for cat in indices)
        content.append(f"- **Total de arquivos**: {total_files:,}")
        content.append(f"- **Categorias principais**: {len(hierarchy)}")
        content.append(f"- **Subcategorias**: {sum(len(hierarchy[cat]['subcategories']) for cat in hierarchy)}")
        content.append("")
        
        # Ordenar categorias por número de arquivos
        sorted_categories = sorted(
            indices.items(),
            key=lambda x: x[1]["total_files"],
            reverse=True
        )
        
        content.append("## 🏷️ Categorias Principais")
        content.append("")
        
        for category, data in sorted_categories:
            description = hierarchy[category]["description"]
            total_files = data["total_files"]
            content.append(f"### {category} ({total_files} arquivos)")
            content.append(f"*{description}*")
            content.append("")
            
            # Listar subcategorias
            if data["subcategories"]:
                content.append("**Subcategorias:**")
                for subcategory, subdata in data["subcategories"].items():
                    subdesc = hierarchy[category]["subcategories"].get(subcategory, "Subcategoria")
                    content.append(f"- **{subcategory}** ({subdata['total_files']} arquivos): {subdesc}")
                content.append("")
            
            # Link para índice detalhado
            content.append(f"📋 [[Indice_{category}|Ver índice detalhado de {category}]]")
            content.append("")
        
        return "\n".join(content)
    
    def generate_category_detail_index(self, category, hierarchy, indices):
        """Gera índice detalhado para uma categoria específica."""
        if category not in indices:
            return None
        
        data = indices[category]
        info = hierarchy[category]
        
        content = []
        content.append(f"# 📂 Índice Detalhado - {category}")
        content.append("")
        content.append(f"*Gerado em: {datetime.now().strftime('%d/%m/%Y %H:%M:%S')}*")
        content.append("")
        
        content.append(f"## 📋 Descrição")
        content.append(f"*{info['description']}*")
        content.append("")
        
        content.append(f"## 📊 Estatísticas")
        content.append(f"- **Total de arquivos**: {data['total_files']:,}")
        content.append(f"- **Subcategorias**: {len(data['subcategories'])}")
        content.append("")
        
        # Subcategorias
        if data["subcategories"]:
            content.append("## 🏷️ Subcategorias")
            content.append("")
            
            # Ordenar subcategorias por número de arquivos
            sorted_subcategories = sorted(
                data["subcategories"].items(),
                key=lambda x: x[1]["total_files"],
                reverse=True
            )
            
            for subcategory, subdata in sorted_subcategories:
                subdesc = info["subcategories"].get(subcategory, "Subcategoria")
                content.append(f"### {subcategory} ({subdata['total_files']} arquivos)")
                content.append(f"*{subdesc}*")
                content.append("")
                
                # Listar arquivos da subcategoria
                if subdata["files"]:
                    content.append("**Arquivos:**")
                    for file_path in sorted(subdata["files"])[:10]:  # Mostrar apenas os 10 primeiros
                        content.append(f"- `{file_path}`")
                    
                    if len(subdata["files"]) > 10:
                        content.append(f"- *... e mais {len(subdata['files']) - 10} arquivos*")
                    content.append("")
        
        # Todos os arquivos da categoria
        content.append("## 📁 Todos os Arquivos")
        content.append("")
        
        if data["files"]:
            for file_path in sorted(data["files"]):
                content.append(f"- `{file_path}`")
        else:
            content.append("*Nenhum arquivo encontrado nesta categoria.*")
        
        content.append("")
        content.append("---")
        content.append("")
        content.append("🔙 [[Indice_Principal_Categorias|← Voltar ao Índice Principal]]")
        
        return "\n".join(content)
    
    def generate_tag_index(self):
        """Gera índice de tags."""
        # Carregar sistema de tags
        tags_path = self.wiki_path / "maps" / "tag_system.json"
        if not tags_path.exists():
            return None
        
        with open(tags_path, "r", encoding="utf-8") as f:
            tag_system = json.load(f)
        
        # Coletar todas as tags
        all_tags = {}
        for file_path, tag_info in tag_system.items():
            for tag in tag_info["tags"]:
                if tag not in all_tags:
                    all_tags[tag] = []
                all_tags[tag].append(file_path)
        
        content = []
        content.append("# 🏷️ Índice de Tags")
        content.append("")
        content.append(f"*Gerado em: {datetime.now().strftime('%d/%m/%Y %H:%M:%S')}*")
        content.append("")
        
        content.append("## 📊 Resumo")
        content.append(f"- **Total de tags únicas**: {len(all_tags)}")
        content.append(f"- **Total de arquivos**: {len(tag_system)}")
        content.append("")
        
        # Ordenar tags por número de arquivos
        sorted_tags = sorted(all_tags.items(), key=lambda x: len(x[1]), reverse=True)
        
        content.append("## 🏷️ Tags Mais Populares")
        content.append("")
        
        for tag, files in sorted_tags[:20]:  # Top 20 tags
            content.append(f"### #{tag} ({len(files)} arquivos)")
            content.append("")
            
            # Mostrar alguns arquivos
            for file_path in sorted(files)[:5]:
                content.append(f"- `{file_path}`")
            
            if len(files) > 5:
                content.append(f"- *... e mais {len(files) - 5} arquivos*")
            content.append("")
        
        content.append("## 📋 Todas as Tags")
        content.append("")
        
        for tag, files in sorted_tags:
            content.append(f"- **#{tag}** ({len(files)} arquivos)")
        
        return "\n".join(content)
    
    def generate_navigation_guide(self, hierarchy, indices):
        """Gera guia de navegação por categoria."""
        content = []
        content.append("# 🧭 Guia de Navegação por Categoria")
        content.append("")
        content.append(f"*Gerado em: {datetime.now().strftime('%d/%m/%Y %H:%M:%S')}*")
        content.append("")
        
        content.append("## 🎯 Como Usar Este Guia")
        content.append("")
        content.append("Este guia organiza toda a documentação da wiki por categorias principais e subcategorias.")
        content.append("Cada categoria tem seu próprio índice detalhado com todos os arquivos organizados.")
        content.append("")
        
        # Ordenar categorias por número de arquivos
        sorted_categories = sorted(
            indices.items(),
            key=lambda x: x[1]["total_files"],
            reverse=True
        )
        
        content.append("## 📂 Categorias Principais")
        content.append("")
        
        for category, data in sorted_categories:
            description = hierarchy[category]["description"]
            total_files = data["total_files"]
            
            content.append(f"### 🏷️ {category}")
            content.append(f"**{total_files} arquivos** - {description}")
            content.append("")
            
            # Subcategorias principais
            if data["subcategories"]:
                content.append("**Subcategorias principais:**")
                sorted_subcategories = sorted(
                    data["subcategories"].items(),
                    key=lambda x: x[1]["total_files"],
                    reverse=True
                )
                
                for subcategory, subdata in sorted_subcategories[:3]:  # Top 3 subcategorias
                    subdesc = hierarchy[category]["subcategories"].get(subcategory, "Subcategoria")
                    content.append(f"- **{subcategory}** ({subdata['total_files']} arquivos): {subdesc}")
                
                if len(data["subcategories"]) > 3:
                    content.append(f"- *... e mais {len(data['subcategories']) - 3} subcategorias*")
                content.append("")
            
            content.append(f"📋 [[Indice_{category}|Ver índice completo de {category}]]")
            content.append("")
        
        content.append("## 🔍 Como Encontrar o que Precisa")
        content.append("")
        content.append("### 👤 Para Iniciantes")
        content.append("- Comece pela categoria **Documentation** → **Guides**")
        content.append("- Consulte **Core** → **Getting_Started**")
        content.append("- Use **Documentation** → **Glossary** para termos técnicos")
        content.append("")
        
        content.append("### 👨‍💻 Para Desenvolvedores")
        content.append("- Foque em **Development** → **API_Reference**")
        content.append("- Consulte **Core** → **Module_System**")
        content.append("- Use **Tools** → **Analysis** para scripts")
        content.append("")
        
        content.append("### 🤖 Para Sistema BMAD")
        content.append("- Acesse **BMAD_System** → **Agents**")
        content.append("- Consulte **BMAD_System** → **Workflows**")
        content.append("- Use **Task_Management** → **Task_Master**")
        content.append("")
        
        content.append("### 🔗 Para Integração")
        content.append("- Foque em **Integration** → **Architecture**")
        content.append("- Consulte **Research** → **Canary_Research**")
        content.append("- Use **Integration** → **Migration**")
        content.append("")
        
        return "\n".join(content)
    
    def run(self):
        """Executa a geração de índices."""
        print("📋 Gerando índices de categoria...")
        
        hierarchy, indices = self.load_categorization_data()
        if not hierarchy or not indices:
            return
        
        # Gerar índices
        files_to_generate = [
            ("Indice_Principal_Categorias.md", self.generate_main_category_index(hierarchy, indices)),
            ("Guia_Navegacao_Categoria.md", self.generate_navigation_guide(hierarchy, indices)),
            ("Indice_Tags.md", self.generate_tag_index())
        ]
        
        # Gerar índices detalhados para cada categoria
        for category in hierarchy.keys():
            detail_index = self.generate_category_detail_index(category, hierarchy, indices)
            if detail_index:
                files_to_generate.append((f"Indice_{category}.md", detail_index))
        
        # Salvar arquivos
        for filename, content in files_to_generate:
            if content:
                file_path = self.wiki_path / filename
                with open(file_path, "w", encoding="utf-8") as f:
                    f.write(content)
                print(f"   ✅ {filename} gerado")
        
        print(f"✅ Índices de categoria gerados com sucesso!")
        print(f"   📁 {len(files_to_generate)} arquivos criados")
        print(f"   📂 {len(hierarchy)} categorias indexadas")
        
        # Estatísticas
        total_files = sum(indices[cat]["total_files"] for cat in indices)
        print(f"   📊 {total_files:,} arquivos organizados")

if __name__ == "__main__":
    generator = CategoryIndexGenerator()
    generator.run() 